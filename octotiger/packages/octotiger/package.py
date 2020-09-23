class Octotiger(CMakePackage):
    """Astrophysics program simulating the evolution of star systems 
        based on the fast multipole method on adaptive Octrees"""

    homepage = "https://github.com/STEllAR-GROUP/octotiger"
    url = "https://github.com/STEllAR-GROUP/octotiger"

    version('octotiger_with_kokkos', git='https://github.com/STEllAR-GROUP/octotiger.git',
            branch='octotiger_with_kokkos')
    version('kokkos_alternative_build', git='https://github.com/STEllAR-GROUP/octotiger.git',
            branch='kokkos_alternative_build')
    version('master', git='https://github.com/STEllAR-GROUP/octotiger.git',
            branch='master')

    variant('cuda', default=True,
            description='Build octotiger with CUDA (also allows Kokkos kernels to run with CUDA)')
    variant('vc', default=True, description='Enable CPU vectorization')
    variant('test', default=True, description='Enable octotiger tests')
    variant('mpi', default=True, description='Build with MPI dependencies')

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


    depends_on('cppuddle')

    depends_on('kokkos-hpx-interop +cuda',
               when='+kokkos +cuda',
               )
    depends_on('kokkos-hpx-interop -cuda',
               when='+kokkos -cuda',
               )

    depends_on('cmake@3.12.4:', type='build')
    depends_on('vc@1.4.1', when='+vc')
    depends_on('boost@1.74.0 cxxstd=14 +mpi', when='+mpi')
    depends_on('boost@1.74.0 cxxstd=14 -mpi', when='-mpi')
    depends_on('hdf5 +mpi +threadsafe +szip +hl ', when='+mpi')
    depends_on('hdf5 -mpi +threadsafe  +szip +hl', when='-mpi')
    depends_on('silo@4.10.2 +mpi ', when='+mpi')
    depends_on('silo@4.10.2 -mpi ', when='-mpi')

    depends_on('cuda', when='+cuda')
    
    hpx_string = 'hpx@1.5.0 cxxstd=14'
    depends_on(hpx_string + ' +cuda', when='+cuda') #networking=mpi ?
    depends_on(hpx_string + ' -cuda', when='-cuda')
    #depends_on(hpx_string + ' +cuda', when='+cuda', patches='header.patch') #networking=mpi ?
    #depends_on(hpx_string + ' -cuda', when='-cuda', patches='header.patch')

    kokkos_string = 'kokkos@3.1 +serial +hpx +hpx_async_dispatch +aggressive_vectorization '
    #depends_on(kokkos_string + ' +cuda +cuda_lambda +wrapper ',
    #           when='+kokkos +cuda',
     #          )
    #depends_on(kokkos_string + ' -cuda -cuda_lambda -wrapper',
   #            when='+kokkos -cuda',
   #            )
    depends_on(kokkos_string + ' +cuda +cuda_lambda +wrapper ', when='+kokkos +cuda', patches=['kokkos_octo_devel.patch'])
    depends_on(kokkos_string + ' -cuda -cuda_lambda -wrapper',when='+kokkos -cuda', patches=['kokkos_octo_devel.patch'])

    depends_on('kokkos-nvcc-wrapper~mpi', when='+kokkos +cuda -mpi',
               patches=['Add-dumpversion-option-to-nvcc_wrapper.patch',
                        'Eval-for-compiler-calls-nvvcc_wrapper.patch']
               )
    depends_on('kokkos-nvcc-wrapper+mpi',
               when='+kokkos +cuda +mpi',
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
        if '+kokkos' in spec and '+cuda' in spec:
            args.append("-DCMAKE_CXX_COMPILER=%s" %
                        self.spec["kokkos-nvcc-wrapper"].kokkos_cxx)

        return args
