class KokkosHpxInterop(CMakePackage):

    url = "https://github.com/msimberg/kokkos-hpx-interop"

    version('master', git='git@github.com:msimberg/kokkos-hpx-interop.git',
        branch='master')

    variant('cuda', default=True)

    depends_on('cmake@3.13.4:', type='build')
    depends_on('hpx@1.4.1 cxxstd=14', 
        patches='diff-from-hpx141-to-msimberg-hpx-ce4ea77805.patch'
    )

    depends_on('cuda', when='+cuda')
    depends_on('kokkos @3.0 +serial +hpx +hpx_async_dispatch std=14', 
        #cxxstd=c++14 # call e.g. for daint  with ^kokkos+pascal60+hsw
        patches='diff-from-kokkos3000-to-msimberg-62acb6051818.patch'
    )
    
    def cmake_args(self):
        spec = self.spec
        args = []

        return args
