class KokkosHpxInterop(CMakePackage):

    url = "https://github.com/STEllAR-GROUP/hpx-kokkos.git"

    version('master', git='https://github.com/STEllAR-GROUP/hpx-kokkos.git',
        branch='master')
    version('stable', git='https://github.com/STEllAR-GROUP/hpx-kokkos.git',
        commit='bc2d2c9caeb2c1d9c4576e504fa3d445f454260b')
    #version('master', git='https://github.com/STEllAR-GROUP/hpx-kokkos.git',
    #    commit='d3b7511c13363359c756c6978f2f752dde16ecaa')

    variant('cuda', default=True)

    depends_on('cmake@3.13.4:', type='build')
    depends_on('hpx cxxstd=14')

    depends_on('cuda', when='+cuda')
    depends_on('kokkos +serial +cuda +cuda_lambda +hpx +hpx_async_dispatch std=14', 
    )
    
    def cmake_args(self):
        spec = self.spec
        args = []
        args.append("-DCMAKE_CXX_COMPILER=%s" %
                    self.spec["kokkos-nvcc-wrapper"].kokkos_cxx) 

        return args
