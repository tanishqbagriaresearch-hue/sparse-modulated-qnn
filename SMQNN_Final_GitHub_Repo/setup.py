from setuptools import setup, find_packages

setup(
    name="SMQNN",
    version="1.0.0",
    author="[Your Name]",
    description="Sparse Modulated Quantum Neural Networks for Barren Plateau Mitigation",
    packages=find_packages(),
    install_requires=[
        "qiskit>=1.0.0",
        "qiskit-aer>=0.13.0",
        "qiskit-ibm-runtime>=0.14.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scipy>=1.11.0",
        "matplotlib>=3.7.0",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
