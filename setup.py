from setuptools import setup, find_packages

setup(
    name="nucleus_tensegrity",
    version="0.1.0",
    author="Hussain Ather, Richard Gordon",
    description="A spatial graph-based model of atomic nuclei based on tensegrity structures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HussainAther/nucleus-tensegrity",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "networkx"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires='>=3.7',
)

