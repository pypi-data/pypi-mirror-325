import unittest
import warnings
import numpy
import atooms.trajectory as trj
import berni
import berni.f90
import berni.lammps
        
try:
    #import rumd
    #import berni.rumd
    #from atooms.backends.rumd import RUMD
    SKIP = False
except ImportError:
    SKIP = True

class TestLAMMPS(unittest.TestCase):

    def _system(self, fname):
        with trj.Trajectory(fname) as th:
            system = th[0]
        system.species_layout = 'F'
        return system

    def _backends_energy(self, system, model):
        import atooms.backends.lammps
        import atooms.backends.f90
        
        # LAMMPS
        # atooms.backends.lammps.lammps_command = 'env/lib/python3.10/site-packages/lammps/lmp'
        cmd = berni.lammps.export(model)
        system.interaction = atooms.backends.lammps.Interaction(cmd)
        epot_lammps = system.potential_energy(per_particle=True)

        # LAMMPS tabulated
        cmd = berni.lammps.export(model, tabulate=True)
        system.interaction = atooms.backends.lammps.Interaction(cmd)
        epot_lammps_tab = system.potential_energy(per_particle=True)
        
        # Atooms
        system.interaction = atooms.backends.f90.Interaction(model)
        epot_f90 = system.potential_energy(per_particle=True)
        
        self.assertAlmostEqual(epot_lammps, epot_f90)
        self.assertAlmostEqual(epot_lammps, epot_lammps_tab)
        
    def _backends_force(self, system, model):
        import atooms.backends.lammps
        import atooms.backends.f90
        
        # LAMMPS
        # atooms.backends.lammps.lammps_command = 'env/lib/python3.10/site-packages/lammps/lmp'
        cmd = berni.lammps.export(model)
        system.interaction = atooms.backends.lammps.Interaction(cmd)
        force_lammps = system.force_norm_square(per_particle=True)

        # LAMMPS tabulated
        cmd = berni.lammps.export(model, tabulate=True)

        # test derivative consistency (from LAMMPS internal test)
        parts = cmd.split('/')
        tmp_dir_hash = parts[2].split()[0]
        tmp_file = f'/tmp/{tmp_dir_hash}/phi.1-1'
        data = numpy.loadtxt(tmp_file, skiprows=5)
        rs = data[:,1]
        us = data[:,2]
        fs = data[:,3]
        ninput = len(data)
        ferror = 0
        for i in range(1, ninput-1):
            r = rs[i]
            rprev = rs[i-1]
            rnext = rs[i+1]
            e = us[i]
            eprev = us[i-1]
            enext = us[i+1]
            f = fs[i]
            fleft = -(e - eprev) / (r - rprev)
            fright = -(enext - e) / (rnext - r)
            if (f < fleft and f < fright): ferror+=1
            if (f > fleft and f > fright): ferror+=1

        system.interaction = atooms.backends.lammps.Interaction(cmd)
        force_lammps_tab = system.force_norm_square(per_particle=True)
        
        # Atooms
        system.interaction = atooms.backends.f90.Interaction(model)
        force_f90 = system.force_norm_square(per_particle=True)
        
        if ferror/ninput>0.01:
            warnings.warn(f'Found {ferror} inconsistencies ({int(ferror/ninput*100)}%) between ' \
                          f'force and -dE/dr (should only be flagged at inflection points).')
        self.assertAlmostEqual(force_lammps, force_f90)
        self.assertAlmostEqual(force_lammps, force_lammps_tab)

    def _supported(self, system, model, backend):
        import atooms.backends.lammps
        import atooms.backends.f90

        if backend == 'lammps':
            cmd = berni.lammps.export(model)
            system.interaction = atooms.backends.lammps.Interaction(cmd)
            _ = system.potential_energy(per_particle=True)
        if backend == 'f90':
            system.interaction = atooms.backends.f90.Interaction(model)
            _ = system.potential_energy(per_particle=True)
            _ = system.force_norm_square(per_particle=True)

    def test_lj(self):
        model = berni.get("lennard_jones")
        fname = berni.samples.get("lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz")
        system = self._system(fname)
        self._backends_energy(system, model)

    def test_ka(self):
        model = berni.models.get('kob_andersen')
        fname = berni.samples.get('kob_andersen-8f4a9fe755e5c1966c10b50c9a53e6bf.xyz')
        system = self._system(fname)
        self._backends_energy(system, model)
        self._backends_force(system, model)

    def test_rhh(self):
        model = berni.models.get('roy_heyde_heuer-II')
        fname = berni.samples.get('roy_heyde_heuer-II-b8d70742799933357ea83314590d2b4d.xyz')
        system = self._system(fname)        
        self._backends_energy(system, model)
        # TODO: fix f90 backend renaming linear_cut_shift
        model = berni.models.get('roy_heyde_heuer-II')
        self._backends_force(system, model)

    def _backend_support(self, backend):
        """Test all potentials"""
        import inspect
        fname = berni.samples.get("lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz")
        system = self._system(fname)
        ignore = {
            'f90': ['fene'],
            'lammps': ['fene']
        }
        unsupported, supported = [], []
        for phi, func in berni.potentials.items():
            if phi in ignore['f90']:
                continue

            args = func.__code__.co_varnames[1:]
            args = inspect.getfullargspec(func)[0]
            defaults = inspect.getfullargspec(func)[3]
            params = {arg: [[default]] for arg, default in zip(args[1:], defaults)}

            model = {
                'potential': [{
                    'type': phi,
                    'parameters': params
                }
                ],
                'cutoff': [{
                    'type': 'cut_shift',
                    'parameters': {'rcut': [[2.5]]}
                }
                ]
            }
            # if phi != 'yukawa': continue
            # print(phi)
            # print(model)
            # self._supported(system, model, backend)
            try:
                self._supported(system, model, backend)
                supported.append(phi)
            except:
                unsupported.append(phi)
        return supported, unsupported

    def test_support_f90(self):
        # print('{} {}'.format(*zip(['YES', 'NO'], self._backend_support('f90'))))
        self._backend_support('f90')

    def test_support_lammps(self):
        # print('{} {}'.format(*zip(['YES', 'NO'], self._backend_support('lammps'))))
        self._backend_support('lammps')

    #def _forces_test(self, system, model):
    def _forces_test(self, phi, cutoff):

        # test derivative consistency (from LAMMPS internal test)
        rs = numpy.linspace(1.0, 3.0, 10000)
        #params={}, cutoff_params={'rcut': 2.5}
        us = [cutoff(phi, params={}, cutoff_params={'rcut': 3.0})(phi)(r)[0] for r in rs]
        fs = [cutoff(phi, params={}, cutoff_params={'rcut': 3.0})(phi)(r)[1] for r in rs]
        ninput = len(rs)
        ferror = 0
        for i in range(1, ninput-1):
            r = rs[i]
            rprev = rs[i-1]
            rnext = rs[i+1]
            e = us[i]
            eprev = us[i-1]
            enext = us[i+1]
            f = fs[i]
            fleft = -(e - eprev) / (r - rprev)
            fright = -(enext - e) / (rnext - r)
            if (f < fleft and f < fright): ferror+=1
            if (f > fleft and f > fright): ferror+=1

        if ferror/ninput>0.01:
            warnings.warn(f'Found {ferror} inconsistencies ({int(ferror/ninput*100)}%) between ' \
                          'force and -dE/dr (should only be flagged at inflection points)')
        # else:
        #     warnings.warn(f'ciao {ferror}')

    # TODO: test forces for all potentials with secants without writing to file
    # def test_forces(self):
    #     """Test all potentials"""
    #     #for phi, func in berni.potentials.items():
    #         #        for cutoff in berni.cutoffs.values():
    #     func = berni.potentials['lennard_jones']

    #     self._forces_test(func, berni.cutoffs['shift'])


if __name__ == '__main__':
    unittest.main()
