class KokkosHpxInterop(CMakePackage):

    url = "https://github.com/msimberg/kokkos-hpx-interop"

    version('master', git='https://github.com/msimberg/kokkos-hpx-interop.git',
        branch='master')

    variant('cuda', default=True)

    depends_on('cmake@3.13.4:', type='build')
    depends_on('hpx@master cxxstd=14')

    depends_on('cuda', when='+cuda')
    depends_on('kokkos@develop +serial +hpx +hpx_async_dispatch std=14', 
    )
    
    def cmake_args(self):
        spec = self.spec
        args = []

        return args
