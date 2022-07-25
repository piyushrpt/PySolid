# Author: Zhang Yunjun, Jan 2021
# Copyright 2020, by the California Institute of Technology.


# always prefer setuptools over distutils
import setuptools
from numpy.distutils.core import setup, Extension

# Grab from version.py file: version
with open("src/pysolid/version.py", "r") as f:
    lines = f.readlines()
    line = [line for line in lines if line.strip().startswith("Tag(")][0].strip()
    version = line.replace("'",'"').split('"')[1]

# specify fortran extensions to build with numpy.f2py
solid_ext = Extension(name='pysolid.solid', sources=['src/pysolid/solid.for'])

setup(
    name='pysolid',
    version=version,
    description="A Python wrapper for solid to compute solid Earth tides",
    url="https://github.com/insarlab/PySolid",
    download_url=("https://github.com/insarlab/PySolid/archive/v{}.tar.gz".format(version)),
    author="Zhang Yunjun, Dennis Milbert",
    author_email="yunjunzgeo@gmail.com",
    license="GPL-3.0-or-later",
    license_files=("LICENSE",),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="solid Eartth tides, deformation, geodesy, geophysics",

    project_urls={
        "Bug Reports": "https://github.com/insarlab/PySolid/issues",
        "Source": "https://github.com/insarlab/PySolid",
    },

    # package discovery
    packages=setuptools.find_packages("src"),  # include all packages under src
    package_dir={"": "src"},                   # tell distutils packages are under src

    # build fortran deps with numpy.f2py
    ext_modules=[solid_ext],

    # dependencies
    python_requires=">=3.6",
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'scikit-image',
    ],

    # data files
    include_package_data=True,
    package_data={
        "pysolid": ["solid.for"],
    },
)
