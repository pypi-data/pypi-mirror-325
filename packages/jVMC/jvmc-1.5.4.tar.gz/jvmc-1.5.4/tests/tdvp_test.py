import unittest

import jax
jax.config.update("jax_enable_x64", True)

import jax.random as random
import jax.numpy as jnp

import numpy as np
from scipy.interpolate import interp1d

import jVMC
import jVMC.global_defs as global_defs
import jVMC.util.stepper as jVMCstepper
import jVMC.nets as nets
from jVMC.vqs import NQS
import jVMC.operator as op
import jVMC.sampler as sampler
import jVMC.mpi_wrapper as mpi

from jVMC.util import measure, ground_state_search

from functools import partial


class TestGsSearch(unittest.TestCase):
    def test_gs_search_cpx(self):
        L = 4
        J = -1.0
        hxs = [-1.3, -0.3]

        exEs = [-6.10160339, -4.09296160]

        for hx, exE in zip(hxs, exEs):
            # Set up variational wave function
            rbm = nets.CpxRBM(numHidden=6, bias=False)
            psi = NQS(rbm)

            # Set up hamiltonian for ground state search
            hamiltonianGS = op.BranchFreeOperator()
            for l in range(L):
                hamiltonianGS.add(op.scal_opstr(J, (op.Sz(l), op.Sz((l + 1) % L))))
                hamiltonianGS.add(op.scal_opstr(hx, (op.Sx(l), )))

            # Set up exact sampler
            exactSampler = sampler.ExactSampler(psi, L)

            delta = 2
            tdvpEquation = jVMC.util.TDVP(exactSampler, snrTol=1, pinvTol=0.0, pinvCutoff=1e-8, rhsPrefactor=1., diagonalShift=delta, makeReal='real')

            # Perform ground state search to get initial state
            ground_state_search(psi, hamiltonianGS, tdvpEquation, exactSampler, numSteps=100, stepSize=5e-2)

            obs = measure({"energy": hamiltonianGS}, psi, exactSampler)

            self.assertTrue(jnp.max(jnp.abs((obs['energy']['mean'] - exE) / exE)) < 1e-3)


class TestTimeEvolution(unittest.TestCase):
    def test_time_evolution(self):
        L = 4
        J = -1.0
        hx = -0.3

        weights = jnp.array(
            [0.23898957, 0.12614753, 0.19479055, 0.17325271, 0.14619853, 0.21392751,
             0.19648707, 0.17103704, -0.15457255, 0.10954413, 0.13228065, -0.14935214,
             -0.09963073, 0.17610707, 0.13386381, -0.14836467]
        )

        global_defs.set_pmap_devices(jax.devices()[0])

        # Set up variational wave function
        rbm = nets.CpxRBM(numHidden=2, bias=False)
        psi = NQS(rbm)
        psi(jnp.array([[[1, 1, 1, 1]]]))
        psi.set_parameters(weights)

        # Set up hamiltonian for time evolution
        hamiltonian = op.BranchFreeOperator()
        for l in range(L):
            hamiltonian.add(op.scal_opstr(J, (op.Sz(l), op.Sz((l + 1) % L))))
            hamiltonian.add(op.scal_opstr(hx, (op.Sx(l), )))

        # Set up ZZ observable
        ZZ = op.BranchFreeOperator()
        for l in range(L):
            ZZ.add((op.Sz(l), op.Sz((l + 1) % L)))

        # Set up exact sampler
        exactSampler = sampler.ExactSampler(psi, L)

        # Set up adaptive time stepper
        stepper = jVMCstepper.AdaptiveHeun(timeStep=1e-3, tol=1e-5)

        tdvpEquation = jVMC.util.TDVP(exactSampler, snrTol=1, pinvTol=0.0, pinvCutoff=1e-8, rhsPrefactor=1.j, diagonalShift=0., makeReal='imag')

        t = 0
        obs = []
        times = []
        times.append(t)
        newMeas = measure({'E': hamiltonian, 'ZZ': ZZ}, psi, exactSampler)
        obs.append([newMeas['E']['mean'], newMeas['ZZ']['mean']])
        while t < 0.5:
            dp, dt = stepper.step(0, tdvpEquation, psi.get_parameters(), hamiltonian=hamiltonian, psi=psi, numSamples=0)
            psi.set_parameters(dp)
            t += dt
            times.append(t)
            newMeas = measure({'E': [(hamiltonian, t)], 'ZZ': ZZ}, psi, exactSampler)
            obs.append([newMeas['E']['mean'], newMeas['ZZ']['mean']])

        obs = np.array(jnp.asarray(obs))

        # Check energy conservation
        obs[:, 0] = np.abs((obs[:, 0] - obs[0, 0]) / obs[0, 0])
        self.assertTrue(np.max(obs[:, 0]) < 1e-3)

        # Check observable dynamics
        zz = interp1d(np.array(times), obs[:, 1, 0])
        refTimes = np.arange(0, 0.5, 0.05)
        netZZ = zz(refTimes)
        refZZ = np.array(
            [0.882762129306284, 0.8936168721790617, 0.9257753299594491, 0.9779836185039352, 1.0482156449061142,
             1.1337654450614298, 1.231369697427413, 1.337354107391303, 1.447796176316155, 1.558696104640795,
             1.666147269524912, 1.7664978782554912, 1.8564960156892512, 1.9334113379450693, 1.9951280521882777,
             2.0402054805651546, 2.067904337137255, 2.078178742959828, 2.071635856483114, 2.049466698269522, 2.049466698269522]
        )
        self.assertTrue(np.max(np.abs(netZZ - refZZ[:len(netZZ)])) < 1e-3)


class TestTimeEvolutionMCSampler(unittest.TestCase):
    def test_time_evolution(self):
        L = 4
        J = -1.0
        hx = -0.3

        weights = jnp.array(
            [0.23898957, 0.12614753, 0.19479055, 0.17325271, 0.14619853, 0.21392751,
             0.19648707, 0.17103704, -0.15457255, 0.10954413, 0.13228065, -0.14935214,
             -0.09963073, 0.17610707, 0.13386381, -0.14836467]
        )

        # Set up variational wave function
        rbm = nets.CpxRBM(numHidden=2, bias=False)
        psi = NQS(rbm, batchSize=5000)
        psi(jnp.array([[[1, 1, 1, 1]]]))
        psi.set_parameters(weights)

        # Set up hamiltonian for time evolution
        hamiltonian = op.BranchFreeOperator()
        for l in range(L):
            hamiltonian.add(op.scal_opstr(J, (op.Sz(l), op.Sz((l + 1) % L))))
            hamiltonian.add(op.scal_opstr(hx, (op.Sx(l), )))

        # Set up ZZ observable
        ZZ = op.BranchFreeOperator()
        for l in range(L):
            ZZ.add((op.Sz(l), op.Sz((l + 1) % L)))

        # Set up exact sampler
        MCsampler = sampler.MCSampler(psi, (L,), jax.random.PRNGKey(0), numSamples=50000, updateProposer=sampler.propose_spin_flip, mu=1, numChains=500)

        # Set up adaptive time stepper
        stepper = jVMCstepper.AdaptiveHeun(timeStep=1e-3, tol=1e-4)

        tdvpEquation = jVMC.util.TDVP(MCsampler, snrTol=1, pinvTol=1e-8, rhsPrefactor=1.j, diagonalShift=0., makeReal='imag', crossValidation=True)

        t = 0
        obs = []
        times = []
        times.append(t)
        newMeas = measure({'E': hamiltonian, 'ZZ': ZZ}, psi, MCsampler)
        obs.append([newMeas['E']['mean'], newMeas['ZZ']['mean']])
        while t < 0.2:
            dp, dt = stepper.step(0, tdvpEquation, psi.get_parameters(), hamiltonian=hamiltonian, psi=psi, numSamples=5000)
            psi.set_parameters(dp)
            t += dt
            times.append(t)
            newMeas = measure({'E': [(hamiltonian, t)], 'ZZ': ZZ}, psi, MCsampler)
            obs.append([newMeas['E']['mean'], newMeas['ZZ']['mean']])

        obs = np.array(jnp.asarray(obs))

        # Check energy conservation
        obs[:, 0] = np.abs((obs[:, 0] - obs[0, 0]) / obs[0, 0])
        self.assertTrue(np.max(obs[:, 0]) < 1e-1)

        # Check observable dynamics
        zz = interp1d(np.array(times), obs[:, 1, 0])
        refTimes = np.arange(0, 0.2, 0.05)
        netZZ = zz(refTimes)
        refZZ = np.array(
            [0.882762129306284, 0.8936168721790617, 0.9257753299594491, 0.9779836185039352, 1.0482156449061142,
             1.1337654450614298, 1.231369697427413, 1.337354107391303, 1.447796176316155, 1.558696104640795,
             1.666147269524912, 1.7664978782554912, 1.8564960156892512, 1.9334113379450693, 1.9951280521882777,
             2.0402054805651546, 2.067904337137255, 2.078178742959828, 2.071635856483114, 2.049466698269522, 2.049466698269522]
        )
        self.assertTrue(np.max(np.abs(netZZ - refZZ[:len(netZZ)])) < 2e-2)


class TestSNRConsistency(unittest.TestCase):
    def test_snr_consistency(self):
        L = 4
        J = -1.0
        hx = -0.3

        weights = jnp.array(
            [0.23898957, 0.12614753, 0.19479055, 0.17325271, 0.14619853, 0.21392751,
             0.19648707, 0.17103704, -0.15457255, 0.10954413, 0.13228065, -0.14935214,
             -0.09963073, 0.17610707, 0.13386381, -0.14836467]
        )

        # Set up variational wave function
        rbm = nets.CpxRBM(numHidden=2, bias=False)
        orbit = jVMC.util.symmetries.get_orbit_1D(L, "translation")
        net = nets.sym_wrapper.SymNet(net=rbm, orbit=orbit)
        psi = NQS(net, batchSize=5000)
        psi(jnp.array([[[1, 1, 1, 1]]]))
        psi.set_parameters(weights)

        # Set up hamiltonian for time evolution
        hamiltonian = op.BranchFreeOperator()
        for l in range(L):
            hamiltonian.add(op.scal_opstr(J, (op.Sz(l), op.Sz((l + 1) % L))))
            hamiltonian.add(op.scal_opstr(hx, (op.Sx(l), )))

        # Set up exact sampler
        sampler = jVMC.sampler.MCSampler(psi, (L,), jax.random.PRNGKey(0), numSamples=10, updateProposer=jVMC.sampler.propose_spin_flip, mu=2, numChains=500)

        # Get sample
        sampleConfigs, sampleLogPsi, p = sampler.sample()

        # Evaluate local energy
        Eloc_old = hamiltonian.get_O_loc(sampleConfigs, psi, sampleLogPsi, 0.0)
        Eloc = jVMC.stats.SampledObs( Eloc_old, p)

        # Evaluate gradients
        sampleGradients_old = psi.gradients(sampleConfigs)
        sampleGradients = jVMC.stats.SampledObs( sampleGradients_old, p)

        self.F0 = (-1.j) * sampleGradients.covar(Eloc).ravel() 
        S = jVMC.util.imagFun( sampleGradients.covar() )

        ev, V = jnp.linalg.eigh(S)

        # old version
        subtract_helper_Eloc = global_defs.pmap_for_my_devices(lambda x, y: x - y, in_axes=(0, None))
        subtract_helper_grad = global_defs.pmap_for_my_devices(lambda x, y: x - y, in_axes=(0, None))
        transform_EO = global_defs.pmap_for_my_devices(lambda eo, v: jnp.matmul(eo, jnp.conj(v)), in_axes=(0, None))
        get_EO = global_defs.pmap_for_my_devices(lambda f, p, Eloc, grad: -f * jnp.multiply((p * Eloc)[:, None], jnp.conj(grad)),
                                                      in_axes=(None, 0, 0, 0), static_broadcasted_argnums=(0))
        Eloc_old = subtract_helper_Eloc(Eloc_old, mpi.global_mean(Eloc_old, p))
        sampleGradients_old = subtract_helper_grad(sampleGradients_old, mpi.global_mean(sampleGradients_old, p))
        EOdata = get_EO(-1., p, Eloc_old, sampleGradients_old) * mpi.globNumSamples
        EOdata = transform_EO(jVMC.util.imagFun(EOdata), V)
        EOdata.block_until_ready()
        rhoVar_old = mpi.global_variance(EOdata, jnp.ones(EOdata.shape[:2]) / mpi.globNumSamples)

        EO = sampleGradients.covar_data(Eloc).transform(linearFun = jnp.transpose(jnp.conj(V)),
                                                        nonLinearFun=lambda x: jVMC.util.imagFun(x))
        rhoVar_new = EO.var().ravel()

        self.assertTrue( jnp.allclose(rhoVar_old, rhoVar_new) )



if __name__ == "__main__":
    unittest.main()
