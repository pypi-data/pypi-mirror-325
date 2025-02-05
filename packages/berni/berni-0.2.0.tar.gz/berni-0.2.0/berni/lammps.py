class UnsupportedPotential(Exception):
    pass


_map = {
    'lennard_jones': 'lj',
    # 'yukawa': 'yukawa',
    'gaussian': 'gauss',
    'cut_shift': 'cut',
    'cut': 'cut',
}

def _fix_gaussian(parameters):
    """Fix sign convention for Gaussian potential"""
    import copy
    import numpy
    parameters = copy.deepcopy(parameters)
    parameters['epsilon'] = - numpy.array(parameters['epsilon'])
    return parameters

# TODO: tabulate missing potentials


_hack = {
    'gaussian': _fix_gaussian
}

_warn = ['cubic_spline', 'quadratic_cut_shift']

def export(model, tabulate=False):
    """Export model as a string with LAMMPS commands"""
    from . import models
    if not hasattr(model, 'get'):
        model = models.get(model, schema_version=1)
    if not tabulate:
        try:
            return _potential_v1(model)
        except UnsupportedPotential:
            pass
    return _tabulate(model)

    # if models.schema_version(model) == 1:
    #     return _potential_v1(model)
    # else:
    #     raise ValueError('unsupported schema for model')

def _tabulate_lammps(potential, npoints=10000, rmin=0.0, rmax=0.0,
                     metadata='', precision=14, **kwargs):
    """Tabulate a potential."""
    from .helpers import tabulate
    rsq, u0, u1, u2 = tabulate(potential, npoints=npoints, rmin=rmin,
                               rmax=rmax, **kwargs)
    r = rsq**0.5
    # The potential returns -u'/r so u1*r will give us the force
    u1 *= r
    txt = f"""

POTENTIAL
N {len(rsq)}

"""
    i = 1
    for x, y, z in zip(r, u0, u1):
        txt += f'{i} {x} {y} {z}\n'
        i += 1
    return txt


def _tabulate_lammps_num(potential, npoints=10000, rmin=0.0, rmax=0.0,
                         metadata='', precision=14, **kwargs):
    """Tabulate a potential."""
    from .helpers import tabulate
    rsq, u0, u1, u2 = tabulate(potential, npoints=npoints, rmin=rmin,
                               rmax=rmax, **kwargs)
    r = rsq**0.5
    # The potential returns -u'/r so u1*r will give us the force
    u1 *= r
    return [r, u0, u1]

def _tabulate_lammps_sum(pot_old, pot_num):
    import numpy
    if pot_old is None:
        return pot_num
    else:
        r_old, u0_old, u1_old = pot_old
        r_new, u0_new, u1_new = pot_num
        assert numpy.all(r_new == r_old)
        return [r_new, u0_old+u0_new, u1_old+u1_new]

def _tabulate_lammps_text(inp):
    """Prepare a tabulated potential for writing to file"""
    r, u0, u1 = inp
    txt = f"""

POTENTIAL
N {len(r)}

"""
    i = 1
    for x, y, z in zip(r, u0, u1):
        txt += f'{i} {x} {y} {z}\n'
        i += 1
    return txt

def _tabulate(model):
    # TODO: refactor

    # assert len(model.get('potential')) == 1
    # assert len(model.get('potential')) in {1, 2}
    assert len(model.get('cutoff')) == len(model.get('potential'))

    from . import potentials, cutoffs
    # print('potentials', help(potentials), dir(potentials))
    # nsp = _guess_species(phi_params)
    nsp = _guess_species(model.get('cutoff')[0].get('parameters'))
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    base = os.path.join(tmpdir, 'phi')
    # pot_file_all = f'{base}.{i+1}-{j+1}'
    # TODO: parametrize npoints
    cmd = ['pair_style table spline 10000']
    pair_coeff = []
    for i in range(nsp):
        for j in range(i, nsp):
            pot_sum = None
            cs_temp = []
            for _cut in model.get('cutoff'):
                cut_params = _cut.get('parameters')
                for key in sorted(cut_params):
                    assert key == 'rcut'
                    cs_temp.append(cut_params[key][i][j])
            rcut_all = max(cs_temp)
            for _phi, _cut in zip(model.get('potential'), model.get('cutoff')):

                phi = _phi.get('type')
                cut = _cut.get('type')
                phi_params = _phi.get('parameters')
                cut_params = _cut.get('parameters')
                ps = {}
                for key in sorted(phi_params):
                    try:
                        ps[key] = phi_params[key][i][j]
                    except TypeError:
                        ps[key] = phi_params[key]
                # ps = {key: phi_params[key][i][j] for key in sorted(phi_params)}
                # cs = {}
                # for key in sorted(cut_params):
                #     if key != 'rcut': cs[key] = cut_params[key][i][j]
                #     else: cs[key] = rcut_all
                cs = {key: cut_params[key][i][j] for key in sorted(cut_params)}
                # We must redecorate the function every time
                func = potentials[phi]
                cutoff = cutoffs[cut]
                _cutoff = cutoff(func, params=ps, cutoff_params=cs)
                func = _cutoff(func)
                # out = _tabulate_lammps(func, rmin=0.1, npoints=10000, overshoot=0, **ps)
                pot_num = _tabulate_lammps_num(func, rmin=0.1, rmax=rcut_all, npoints=10000, overshoot=0, **ps)
                pot_sum = _tabulate_lammps_sum(pot_sum, pot_num)
            pot_file = f'{base}.{i+1}-{j+1}'
            with open(pot_file, 'w') as fh:
                pot_text = _tabulate_lammps_text(pot_sum)
                fh.write(pot_text)
            cmd.append(f'pair_coeff {i+1} {j+1} {pot_file} POTENTIAL')
    # for line in cmd:
    #    print(line)
    return '\n'.join(cmd).strip()

def _guess_species(phi_params):
    nsp = 0
    for key in phi_params:
        try:
            nsp = len(phi_params[key])
            return nsp
        except TypeError:
            continue
    raise ValueError('could not find number of species')

def _guess_species(phi_params):
    nsp = 0
    for key in phi_params:
        try:
            nsp = len(phi_params[key])
            return nsp
        except TypeError:
            continue
    raise ValueError('could not find number of species')

def _potential_v1(model):
    # At this stage we expect a model dictionary
    # As of now, we only support one potential with lammps

    try:
        assert len(model.get('potential')) == 1
        assert len(model.get('cutoff')) == 1
    except AssertionError:
        raise UnsupportedPotential
    phi = model.get('potential')[0].get('type')
    cut = model.get('cutoff')[0].get('type')
    phi_params = model.get('potential')[0].get('parameters')
    cut_params = model.get('cutoff')[0].get('parameters')
    if phi in _hack:
        phi_params = _hack[phi](phi_params)

    nsp = _guess_species(phi_params)
    try:
        _phi = _map[phi]
        _cut = _map[cut]
    except KeyError:
        raise UnsupportedPotential
    # We must set a dummy cutoff here, but it will be overwritten later
    pair_style = f'pair_style {_phi}/{_cut} 1.0'
    # Some styles do not accept the cut option
    # and only have a global cutoff
    pair_coeff = []
    for i in range(nsp):
        for j in range(i, nsp):
            ps = []
            for entry in sorted(phi_params):
                ps.append(phi_params[entry][i][j])
            ps.append(cut_params['rcut'][i][j])
            ps = ' '.join([str(_) for _ in ps])
            pair_coeff.append(f'pair_coeff {i+1} {j+1} {ps}')
    pair_coeff = '\n'.join(pair_coeff)
    pair_modify = ''
    if 'shift' in cut:
        pair_modify = 'pair_modify shift yes'

    cmd = '\n'.join([pair_style, pair_coeff, pair_modify]).strip()
    return cmd
