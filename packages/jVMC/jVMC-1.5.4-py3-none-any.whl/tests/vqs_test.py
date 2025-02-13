import unittest

import jVMC
import jVMC.nets as nets
from jVMC.vqs import NQS

import jVMC.global_defs as global_defs

import jax
import jax.numpy as jnp
import numpy as np
from math import isclose

import flax.linen as nn
import jVMC.nets.activation_functions as act_funs


def get_shape(shape):
    return (global_defs.myDeviceCount,) + shape


class CpxRBM_nonHolomorphic(nn.Module):
    """Restricted Boltzmann machine with complex parameters.

    Initialization arguments:
        * ``s``: Computational basis configuration.
        * ``numHidden``: Number of hidden units.
        * ``bias``: ``Boolean`` indicating whether to use bias.

    """
    numHidden: int = 2
    bias: bool = False

    @nn.compact
    def __call__(self, s):

        layer = nn.Dense(self.numHidden, use_bias=self.bias,
                         **jVMC.nets.initializers.init_fn_args(kernel_init=jVMC.nets.initializers.cplx_init,
                                        bias_init=jax.nn.initializers.zeros,
                                        dtype=global_defs.tCpx)
                         )

        out = layer(2 * s.ravel() - 1)
        out = out + jnp.real(out) * 1e-2
        return jnp.sum(act_funs.log_cosh(out))

# ** end class CpxRBM_nonHolomorphic

class Simple_nonHolomorphic(nn.Module):
    """Restricted Boltzmann machine with complex parameters.

    Initialization arguments:
        * ``s``: Computational basis configuration.
        * ``numHidden``: Number of hidden units.
        * ``bias``: ``Boolean`` indicating whether to use bias.

    """
    numHidden: int = 2
    bias: bool = False

    @nn.compact
    def __call__(self, s):

        z = self.param('z', jVMC.nets.initializers.cplx_init, (1,), global_defs.tCpx)
    
        return jnp.sum(jnp.conj(z))

# ** end class Simple_nonHolomorphic

class MatrixMultiplication_NonHolomorphic(nn.Module):
    holo: bool = False

    @nn.compact
    def __call__(self, s):
        layer1 = nn.Dense(1, use_bias=False, **jVMC.nets.initializers.init_fn_args(dtype=global_defs.tCpx))
        out = layer1(2 * s.ravel() - 1)
        if not self.holo:
            out = out + 1e-1 * jnp.real(out)
        return jnp.sum(out)
    
# ** end class MatrixMultiplication_NonHolomorphic


class TestGradients(unittest.TestCase):

    def test_automatic_holomorphicity_recognition(self):

        for k in range(10):
            L = 3
            rbm = nets.CpxRBM(numHidden=2**k, bias=True)
            orbit = jVMC.util.symmetries.get_orbit_1D(L)
            net = nets.sym_wrapper.SymNet(net=rbm, orbit=orbit)
            s = jnp.zeros(get_shape((4, 3)), dtype=np.int32)
            psiC = NQS(net)
            psiC(s)

            self.assertTrue(psiC.holomorphic)

    def test_gradients_cpx(self):

        dlist = [jax.devices()[0], jax.devices()]

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            L = 3
            rbm = nets.CpxRBM(numHidden=2, bias=True)

            orbit = jVMC.util.symmetries.get_orbit_1D(L)
            net = nets.sym_wrapper.SymNet(net=rbm, orbit=orbit)
            psiC = NQS(net)

            s = jnp.zeros(get_shape((4, 3)), dtype=np.int32)
            s = s.at[..., 0, 1].set(1)
            s = s.at[..., 2, 2].set(1)

            psi0 = psiC(s)
            G = psiC.gradients(s)
            delta = 1e-6
            params = psiC.get_parameters()
            for j in range(G.shape[-1]):
                u = jnp.zeros(G.shape[-1], dtype=global_defs.tReal).at[j].set(1)
                psiC.update_parameters(delta * u)
                psi1 = psiC(s)
                psiC.set_parameters(params)

                # Finite difference gradients
                Gfd = (psi1 - psi0) / delta
                with self.subTest(i=j):
                    self.assertTrue(jnp.max(jnp.abs(Gfd - G[..., j])) < 1e-2)

    def test_gradients_real(self):

        dlist = [jax.devices()[0], jax.devices()]

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            L = 3
            rbmModel1 = nets.RBM(numHidden=2, bias=True)
            rbmModel2 = nets.RBM(numHidden=3, bias=True)
            psi = NQS((rbmModel1, rbmModel2))

            s = jnp.zeros(get_shape((4, 3)), dtype=np.int32)
            s = s.at[..., 0, 1].set(1)
            s = s.at[..., 2, 2].set(1)

            psi0 = psi(s)
            G = psi.gradients(s)
            delta = 1e-5
            params = psi.get_parameters()
            for j in range(G.shape[-1]):
                u = jnp.zeros(G.shape[-1], dtype=jVMC.global_defs.tReal).at[j].set(1)
                psi.update_parameters(delta * u)
                psi1 = psi(s)
                psi.set_parameters(params)

                # Finite difference gradients
                Gfd = (psi1 - psi0) / delta

                with self.subTest(i=j):
                    self.assertTrue(jnp.max(jnp.abs(Gfd - G[..., j])) < 1e-2)

    def test_gradients_nonholomorphic(self):

        dlist = [jax.devices()[0], jax.devices()]

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            L = 3
            model = nets.RNN1DGeneral(L=L)
            psi = NQS(model)

            s = jnp.zeros(get_shape((4, 3)), dtype=np.int32)
            s = s.at[..., 0, 1].set(1)
            s = s.at[..., 2, 2].set(1)

            psi0 = psi(s)
            G = psi.gradients(s)
            delta = 1e-5
            params = psi.get_parameters()
            for j in range(G.shape[-1]):
                u = jnp.zeros(G.shape[-1], dtype=jVMC.global_defs.tReal).at[j].set(1)
                psi.update_parameters(delta * u)
                psi1 = psi(s)
                psi.set_parameters(params)

                # Finite difference gradients
                Gfd = (psi1 - psi0) / delta

                with self.subTest(i=j):
                    self.assertTrue(jnp.max(jnp.abs(Gfd - G[..., j])) < 1e-2)

    
    def test_gradients_complex_nonholomorphic(self):
        
        dlist=[jax.devices()[0], jax.devices()]

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            model = Simple_nonHolomorphic()

            s=jnp.zeros(get_shape((4,3)),dtype=np.int32)
            s=s.at[...,0,1].set(1)
            s=s.at[...,2,2].set(1)
            
            psi = NQS(model)
            psi0 = psi(s)
            G = psi.gradients(s)
            delta=1e-5
            params = psi.get_parameters()
            for j in range(G.shape[-1]):
                u = jnp.zeros(G.shape[-1], dtype=jVMC.global_defs.tCpx).at[j].set(1)
                psi.update_parameters(delta * u)
                psi1 = psi(s)
                psi.set_parameters(params)

                # Finite difference gradients
                Gfd = (psi1-psi0) / delta

                with self.subTest(i=j):
                    self.assertTrue( jnp.max( jnp.abs( Gfd - G[...,j] ) ) < 1e-2 )
        
        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            model = CpxRBM_nonHolomorphic()

            s=jnp.zeros(get_shape((4,3)),dtype=np.int32)
            s=s.at[...,0,1].set(1)
            s=s.at[...,2,2].set(1)
            
            psi = NQS(model)
            psi0 = psi(s)
            G = psi.gradients(s)
            delta=1e-5
            params = psi.get_parameters()
            for j in range(G.shape[-1]):
                u = jnp.zeros(G.shape[-1], dtype=jVMC.global_defs.tCpx).at[j].set(1)
                psi.update_parameters(delta * u)
                psi1 = psi(s)
                psi.set_parameters(params)

                # Finite difference gradients
                Gfd = (psi1-psi0) / delta

                with self.subTest(i=j):
                    self.assertTrue( jnp.max( jnp.abs( Gfd - G[...,j] ) ) < 1e-2 )

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            model = MatrixMultiplication_NonHolomorphic(holo=False)

            s=jnp.zeros(get_shape((1,4)),dtype=np.int32)
            
            psi = NQS(model)
            psi0 = psi(s)
            G = psi.gradients(s)
            ref = jnp.array([-1.1+0.j, -1.1+0.j, -1.1+0.j, -1.1+0.j, -0.-1.j, -0.-1.j, -0.-1.j, -0.-1.j])
            self.assertTrue( jnp.allclose( G.ravel(), ref ) )


    def test_gradient_dict(self):
        
        dlist=[[jax.devices()[0],], jax.devices()]

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            net = jVMC.nets.CpxRBM(numHidden=8, bias=False)
            psi = jVMC.vqs.NQS(net, seed=1234)  # Variational wave function

            s = jnp.zeros((len(ds),3,4))
            psi(s)

            g1 = psi.gradients(s)
            g2 = psi.gradients_dict(s)["Dense_0"]["kernel"]

            self.assertTrue(isclose(jnp.linalg.norm(g1-g2),0.0))

class TestEvaluation(unittest.TestCase):

    def test_evaluation_cpx(self):

        dlist = [jax.devices()[0], jax.devices()]

        for ds in dlist:

            global_defs.set_pmap_devices(ds)

            L = 3
            model = nets.CpxRBM(numHidden=2, bias=True)
            psiC = NQS(model)

            s = jnp.zeros(get_shape((4, L)), dtype=np.int32)
            s = s.at[..., 0, 1].set(1)
            s = s.at[..., 2, 2].set(1)

            cpxCoeffs = psiC(s)
            f, p = psiC.get_sampler_net()
            realCoeffs = global_defs.pmap_for_my_devices(lambda x: jax.vmap(lambda y: f(p, y))(x))(s)

            self.assertTrue(jnp.linalg.norm(jnp.real(cpxCoeffs) - realCoeffs) < 1e-6)


if __name__ == "__main__":
    unittest.main()
