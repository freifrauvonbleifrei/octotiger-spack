class Cppuddle(CMakePackage): 

    url = "https://github.com/G-071/hpx-kokkos-interopt-WIP"

    version('master', git='https://github.com/G-071/hpx-kokkos-interopt-WIP.git',
        branch='master')

    variant('counters', default=False, description='Build with allocation counters enabled.')

    def cmake_args(self):
        spec = self.spec
        args = []

        args += [
            self.define_from_variant('CPPUDDLE_WITH_COUNTERS', 'counters'),
        ]
        return args
