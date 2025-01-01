from setuptools import setup, find_packages

setup(
    name="mbSTATS",
    version="0.0.2",  
    author="Satvik",
    author_email="f20213047@goa.bits-pilani.ac.in",
    description="A library for statistical analysis of metabolomics data",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "matplotlib",
        "seaborn",
        "scikit-learn"
    ],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'mbstats-cli=mbSTATS.cli:main',  
        ],
    },
)
