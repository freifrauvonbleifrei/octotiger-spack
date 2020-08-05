class Cppuddle(CMakePackage): 

    url = "https://github.com/G-071/hpx-kokkos-interopt-WIP"

    version('master', git='https://github.com/G-071/hpx-kokkos-interopt-WIP.git',
        branch='master')

    def cmake_args(self):
        spec = self.spec
        args = []
        return args
