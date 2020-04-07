# Octotiger Spack Repository

This repo will be the most up-to-date location for Spack packages for Octotiger.

## Getting Started

Make sure you have downloaded [Spack](https://github.com/spack/spack) and added it to your path.
The easiest way to do this is often (depending on your SHELL):
````
> source spack/share/spack/setup-env.sh
````

After downloading the octotiger-spack GitHub repository, you need to add the kokkos-spack repository according to the instructions on their [Github Page](https://github.com/kokkos/kokkos-spack).

Then, to add the octotiger spack package, you simply need to run
````
> spack repo add octotiger-spack/octotiger
````

To validate that Spack now sees the repo with the Octotiger packages, run:
````
> spack repo list
````
This should now list your newly downloaded Spack repo.
You can display information about how to install the packages with:
````
> spack info octotiger
````
This will print all the information about how to install Octotiger with Spack.

To allow octotiger to be built with the right variants of hpx and kokkos, it is best to specify those manually, e.g. for piz daint:
````
> spack spec octotiger +cuda +kokkos ^hpx cuda_arch=60 ^kokkos cuda_arch=60 +pascal60 +hsw
````

This command here can be run in the build directory, to produce a `spconfig.py` file as a drop-in for the cmake call...
````
> spack setup octotiger@master +cuda +kokkos ^hpx cuda_arch=60 ^kokkos cuda_arch=60 +pascal60 +hsw
````

...which can be used for development builds.
````
> python spconfig.py -DCMAKE_CUDA_FLAGS="-arch=sm_60" ../octotiger
````

If you encounter an error with `spack setup` and `'SPACK_DEPENDENCIES'`, it is connected to the issue described here:
https://github.com/spack/spack/pull/10715

and can be fixed either by executing
````
> export SPACK_DEPENDENCIES=
````
each time, or doing this here once
````
git fetch git@github.com:spack/spack.git refs/pull/10715/head
git merge FETCH_HEAD
````
in the spack repo (only necessary as long as the PR is not yet merged).

For detailed instructions on how to use Spack, see the [User Manual](https://spack.readthedocs.io).

Most of this README was shamelessly adapted from [Kokkos' Spack Repository](https://github.com/kokkos/kokkos-spack), which we refer to for further instructions and links.
