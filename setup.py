from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
setup(
    name = "GaussFunction",
    ext_modules=[
        Extension("gauss", ["gauss.pyx"])
    ],
    cmdclass = {'build_ext': build_ext}
)