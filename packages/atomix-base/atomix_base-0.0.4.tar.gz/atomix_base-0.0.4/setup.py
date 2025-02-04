from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.4"

ext_modules = [
    Pybind11Extension(
        "atomix_base",
        ["src/main.cpp"],
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="atomix_base",
    version=__version__,
    author="0xDEADFED5",
    author_email="admin@terminoid.com",
    url="https://github.com/0xDEADFED5/pyatomix",
    description="C++ atomics for pyatomix",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
