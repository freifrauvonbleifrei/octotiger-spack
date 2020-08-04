class KokkosHpxInterop(CMakePackage):

    url = "https://github.com/STEllAR-GROUP/hpx-kokkos.git"

    #version('master', git='https://github.com/STEllAR-GROUP/hpx-kokkos.git',
     #   branch='master')
    version('master', git='https://github.com/STEllAR-GROUP/hpx-kokkos.git',
        commit='d3b7511c13363359c756c6978f2f752dde16ecaa')
    #patch('fix_header_install.patch')

    variant('cuda', default=True)

    depends_on('cmake@3.13.4:', type='build')
    depends_on('hpx@master cxxstd=14')

    depends_on('cuda', when='+cuda')
    depends_on('kokkos +serial +hpx +hpx_async_dispatch std=14', 
    )
    
    def cmake_args(self):
        spec = self.spec
        args = []

        return args
