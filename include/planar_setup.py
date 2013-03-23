from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
setup(
    name = "PlanarFunction",
    ext_modules=[
        Extension("planar", ["planar.pyx"])
    ],
    cmdclass = {'build_ext': build_ext}
)