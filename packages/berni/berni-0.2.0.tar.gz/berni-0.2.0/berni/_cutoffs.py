import numpy as np
from .helpers import _objdict

__all__ = ['shift', 'cut', 'linear', 'quadratic',
           'quadratic_cut_shift', 'linear_cut_shift', 'cut_shift']

class shift:

    # def __init__(self, func, params, cutoff_params):
    #     cutoff_params['rcut'] = np.array(cutoff_params['rcut'])
    #     nsp = cutoff_params['rcut'].shape[0]
    #     cutoff_params['shift'] = np.ndarray((nsp, nsp))
    #     for isp in range(nsp):
    #         for jsp in range(nsp):
    #             cutoff_params['shift'][isp, jsp] = func(cutoff_params['rcut'][isp, jsp], isp, jsp, **params)[0]
    #     # Somehow jax only accepts a reference to a dict
    #     self._params = cutoff_params
    #     self._func = func

    def __init__(self, func, params, cutoff_params):
        cutoff_params['rcut'] = np.array(cutoff_params['rcut'])
        cutoff_params['shift'] = func(cutoff_params['rcut'], **params)[0]
        self._params = cutoff_params
        self._func = func

    def __call__(self, func):
        def wrapper(r, *args, **kwargs):
            return self._func(r, *args, **kwargs) - np.array([self._params['shift'], 0., 0.])
        wrapper._params = self._params
        return wrapper

class cut:

    def __init__(self, func, params, cutoff_params):
        cutoff_params['rcut'] = np.array(cutoff_params['rcut'])
        # self._params = cutoff_params
        self._func = func

    def __call__(self, func):
        def wrapper(r, *args, **kwargs):
            return self._func(r, *args, **kwargs)
        # wrapper._params = self._params
        return wrapper

# class linear:
#    pass

class linear:
    def __init__(self, func, params, cutoff_params):

        # reminder: func returns u, -u'/r, ? as u0, u1, u2
        cutoff_params['rcut'] = np.array(cutoff_params['rcut'])
        cutoff_params['shift'] = func(cutoff_params['rcut'], **params)[0]
        cutoff_params['deriv'] = func(cutoff_params['rcut'], **params)[1]
        cutoff_params['m'] = + cutoff_params['rcut'] * cutoff_params['deriv']
        cutoff_params['q'] = - cutoff_params['shift'] - cutoff_params['m']*cutoff_params['rcut']
        self._params = cutoff_params
        self._func = func

    def __call__(self, func):
        def wrapper(r, *args, **kwargs):
            v0 = self._func(r, *args, **kwargs)[0] + (self._params['m']*r + self._params['q'])
            v1 = self._func(r, *args, **kwargs)[1] - self._params['m']/r  # self._params['rcut']
            v2 = self._func(r, *args, **kwargs)[2]
            return [v0, v1, v2]
        wrapper._params = self._params
        return wrapper

class quadratic:
    pass

class cubic_spline:
    pass


cut_shift = shift
linear_cut_shift = linear
quadratic_cut_shift = quadratic
