# class HpxKokkosInteroptWip(Package):
class HpxKokkosInteroptWip(CMakePackage): # only headers are currently used

    url = "https://github.com/G-071/hpx-kokkos-interopt-WIP"

    version('master', git='https://github.com/G-071/hpx-kokkos-interopt-WIP.git',
        branch='master')

    variant('cuda', default=True)
    variant('mpi', default=True)

    depends_on('kokkos-hpx-interop')
    
    depends_on('cmake@3.13.4:', type='build')
    depends_on('hpx@1.4.1 cxxstd=14', 
        # patches='diff-from-hpx141-to-msimberg-hpx-ce4ea77805.patch'
    )
    depends_on('cuda', when='+cuda')
    depends_on('kokkos @3.0 +serial +hpx +hpx_async_dispatch std=14',
        # patches='diff-from-kokkos3000-to-msimberg-62acb6051818.patch'
    )
    depends_on('kokkos-nvcc-wrapper~mpi',
               when='+cuda~mpi'
               )
    depends_on('kokkos-nvcc-wrapper+mpi',
               when='+cuda+mpi'
               )
    
    def cmake_args(self):
        spec = self.spec
        args = []
        args.append(self.define_from_variant('INTEROPT_WITH_CUDA', 'cuda'))
        if '+cuda' in spec:
            args.append("-DCMAKE_CXX_COMPILER=%s" %
                        self.spec["kokkos-nvcc-wrapper"].kokkos_cxx)

        return args
