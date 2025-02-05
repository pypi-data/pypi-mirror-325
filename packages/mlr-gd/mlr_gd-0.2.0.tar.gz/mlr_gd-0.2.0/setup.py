from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="mlr-gd",
    version="0.2.0",
    description="A package for multiple linear regression by gradient descent.",
    packages=find_packages(exclude=['tests']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrSolidDevil/mlr-gd/",
    author="DrSolidDevil",
    license="BSD 3-Clause",
    keywords=[
        "linear regression",
        "linear",
        "regression",
        "gradient descent",
        "machine learning",
        "artificial intelligence"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    install_requires=["numpy >= 2.2.1"],
    extras_require={
        "dev": ["twine>=6.0.1", "pandas>=2.2.3", "pytest>=8.3.4", "setuptools>=75.8.0"],
    },
    python_requires=">=3.11",
)
