#!/usr/bin/env python

import glob
import subprocess
import sys
from distutils.command.build_ext import build_ext
from distutils.core import Extension, setup


class build_ext_subclass(build_ext):
    def build_extensions(self):
        self.compiler.define_macro("PYTHON_MAJOR_VERSION", sys.version_info[0])
        print("Testing for std::tr1::shared_ptr...")
        try:
            self.compiler.compile(["test_std_tr1_shared_ptr.cpp"])
            self.compiler.define_macro("HAVE_STD_TR1_SHARED_PTR")
            print("...found")
        except:
            print(" ...not found")

        print("Testing for std::shared_ptr...")
        try:
            self.compiler.compile(["test_std_shared_ptr.cpp"], extra_preargs=["-std=c++0x"]),
            self.compiler.define_macro("HAVE_STD_SHARED_PTR")
            print("...found")
        except:
            print("...not found")

        print("Testing for std::unique_ptr...")
        try:
            self.compiler.compile(["test_std_unique_ptr.cpp"], extra_preargs=["-std=c++0x"]),
            self.compiler.define_macro("HAVE_STD_UNIQUE_PTR")
            print("...found")
        except:
            print("...not found")

        build_ext.build_extensions(self)


# Remove the "-Wstrict-prototypes" compiler option, which isn't valid for C++.
import distutils.sysconfig

cfg_vars = distutils.sysconfig.get_config_vars()
for key, value in cfg_vars.items():
    if type(value) == str:
        cfg_vars[key] = value.replace("-Wstrict-prototypes", "")

with open("LICENSE") as file:
    license = file.read()

extra_compile_args = [
    "-std=c++0x",
    "-Wno-deprecated",
    "-Wno-unused-variable",
    "-Wno-deprecated-declarations",
    "-Wno-uninitialized",
    "-Wno-unused-label",
    "-IC++/swig",
    "-DHAVE_SSL=1",
]

ldflags = subprocess.getoutput("pkg-config --libs openssl").strip().split()
extra_link_args = ldflags

if sys.platform == "linux":  # TODO: execute command  to get openssl
    extra_compile_args.append("-I/usr/include/openssl")
else:
    extra_compile_args.append("-I/usr/local/Cellar/openssl@3/3.3.0/include")

setup(
    name="qfpatch",
    version="2.0.0",
    python_requires=">=3.9",
    py_modules=[
        "quickfix",
        "quickfixt11",
        "quickfix40",
        "quickfix41",
        "quickfix42",
        "quickfix43",
        "quickfix44",
        "quickfix50",
        "quickfix50sp1",
        "quickfix50sp2",
    ],
    data_files=[("share/quickfix", glob.glob("spec/FIX*.xml"))],
    author_email="mackley@connamara.com",
    maintainer="Michael Ackley",
    maintainer_email="mackley@connamara.com",
    description="Python package for Quickfix C++, FIX (Financial Information eXchange) protocol implementation",
    url="https://github.com/quickfix/quickfix",
    download_url="https://github.com/quickfix/quickfix",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=license,
    cmdclass={"build_ext": build_ext_subclass},
    ext_modules=[
        Extension(
            "_quickfix",
            glob.glob("C++/*.cpp"),
            include_dirs=["C++"],
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args,
            libraries=["ssl", "crypto"],
        )
    ],
)
