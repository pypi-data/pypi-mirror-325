from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "ctc_forced_aligner.align_ops",  # Use a submodule for clarity
        ["ctc_forced_aligner/main.cpp"],  # Ensure correct path
        cxx_std=17,  # Use C++17 standard
    ),
]

# Setup configuration
setup(
    name="ctc_forced_aligner",
    version="1.0.0",
    author="Deskpai",
    author_email="dev@deskpai.com",
    description="CTC Forced Alignment",
    packages=find_packages(),  # Include all Python packages
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    install_requires=[
        "requests>=2.32.3",
        "librosa>=0.10.2.post1",
        "numpy==1.26.3",
        "onnxruntime>=1.20.1"
    ],
    package_data={
        "ctc_forced_aligner": ["punctuations.lst"],  # Include punctuations.lst in package
    },
    options={
        'build_ext': {
            'inplace': True,  # Build the shared library in the source directory
        },
    },
)
