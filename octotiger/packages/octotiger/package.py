class Octotiger(CMakePackage):
    """Astrophysics program simulating the evolution of star systems 
        based on the fast multipole method on adaptive Octrees"""

    homepage = "https://github.com/STEllAR-GROUP/octotiger"
    url = "https://github.com/STEllAR-GROUP/octotiger"

    version('octotiger_with_kokkos', git='https://github.com/STEllAR-GROUP/octotiger.git',
            branch='octotiger_with_kokkos')
    version('master', git='https://github.com/STEllAR-GROUP/octotiger.git',
            branch='master')

    variant('cuda', default=True,
            description='Build octotiger fmm kernels with CUDA directly, not only the Kokkos/HPX parallel magic')
    variant('vc', default=True, description='Enable CPU vectorization')
    variant('test', default=True, description='Enable octotiger tests')

    variant(
        'griddim', default='8', description='Octotiger grid size',
        values=('8'), multi=False
    )
    variant(
        'theta_minimum', default='0.34', description='Octotiger minimal allowed theta value',
        values=('0.34', '0.5', '0.16'), multi=False
    )
    variant('kokkos', default=True,
            description='Build octotiger with kokkos based kernels')


    depends_on('hpx-kokkos-interopt-wip',
               when='+kokkos',
               )

    depends_on('kokkos-hpx-interop',
               when='+kokkos',
               )

    depends_on('cmake@3.10:', type='build')
    depends_on('vc@1.4.1', when='+vc')
    depends_on('boost')
    depends_on('hdf5@:1.10.999 +mpi +cxx')
    depends_on('silo+mpi')
    depends_on('hpx@1.4.1 +cuda cxxstd=14')

    depends_on('cuda', when='+cuda')
    depends_on('kokkos @3.0 +serial +cuda +cuda_lambda +hpx +hpx_async_dispatch +wrapper std=14',
               # cxxstd=c++14 # call e.g. for daint  with ^kokkos+pascal60+hsw
               when='+kokkos',
               )
    depends_on('kokkos-nvcc-wrapper',
               when='+kokkos',
               patches=['Add-dumpversion-option-to-nvcc_wrapper.patch',
                        'Eval-for-compiler-calls-nvvcc_wrapper.patch']
               )

    def cmake_args(self):
        spec = self.spec
        args = []

        # CUDA
        args.append(self.define_from_variant('OCTOTIGER_WITH_CUDA', 'cuda'))

        # Vc
        args.append(self.define_from_variant('OCTOTIGER_WITH_Vc', 'vc'))

        # test
        args.append(self.define_from_variant('OCTOTIGER_WITH_TESTS', 'test'))

        # griddim
        args.append(
            '-DOCTOTIGER_WITH_GRIDDIM={0}'.format(spec.variants['griddim'].value))

        # theta_minimum
        args.append(
            '-DOCTOTIGER_THETA_MINIMUM={0}'.format(spec.variants['theta_minimum'].value))

        # Kokkos
        args.append(self.define_from_variant('OCTOTIGER_WITH_KOKKOS', 'kokkos'))

        # set nvcc_wrapper as compiler
        if '+kokkos' in spec:
            args.append("-DCMAKE_CXX_COMPILER=%s" %
                        self.spec["kokkos-nvcc-wrapper"].kokkos_cxx)

        return args
