from setuptools import setup, find_packages

setup(
    name="NSDQ",
    version="0.2.0",
    packages=find_packages(),
    install_requires=["seaborn", "requests", "pandas", "py_vollib_vectorized", "scipy", "matplotlib", "numpy"],
)
