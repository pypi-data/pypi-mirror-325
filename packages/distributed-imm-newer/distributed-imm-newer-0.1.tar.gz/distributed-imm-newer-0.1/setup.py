import os
import sys
import numpy
from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize
import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

# Detect version directory, default to "version-1"
version_dir = os.getenv("IMM_VERSION", "version-1")

# Ensure the specified version directory exists
if not os.path.isdir(f"d-imm-python/{version_dir}"):
    raise ValueError(f"Specified version directory 'd-imm-python/{version_dir}' does not exist.")

# Handling Cython extensions
if '--cython' in sys.argv:
    extensions = [
        Extension(
            "cut_finder",
            # [f"d-imm-python/{version_dir}/splitters/cut_finder.pyx"],
            [f"splitters/cut_finder.pyx"],

            extra_compile_args=['-fopenmp'],
            extra_link_args=['-fopenmp'],
            include_dirs=[numpy.get_include()]
        )
    ]
    extensions = cythonize(extensions, annotate=True)
    sys.argv.remove("--cython")
else:
    extensions = [
        Extension(
            "cut_finder",
            [f"splitters/cut_finder.c"],
            include_dirs=[numpy.get_include()]
        )
    ]

setup(
    name="distributed-imm-newer",
    version="0.1",
    description="A distributed implementation of the IMM algorithm for explaining clusters in Spark ML pipelines.",
    author="saadha",
    author_email="marium.20@cse.mrt.ac.lk",
    packages=find_packages(where=f"d-imm-python/{version_dir}"),
    package_dir={"": f"d-imm-python/{version_dir}"},
    install_requires=[
        "pyspark>=3.0.0",
        "scikit-learn",
        "pandas",
        "numpy",
        "graphviz",
        "cython"
    ],
    python_requires=">=3.6",
    include_package_data=True,
    ext_modules=extensions,
    zip_safe=False
)
