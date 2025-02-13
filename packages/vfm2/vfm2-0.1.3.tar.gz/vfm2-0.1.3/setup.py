from setuptools import setup, find_packages


setup(
    name="vfm2", 
    version="0.1.3",  # current version
    author="Jose Torraca & Daniel Silva",  
    author_email="joseneto@eq.ufrj.br",  
    description="Virtual Flow Meter with delumping",
    long_description=open("README.md", "r").read(), 
    long_description_content_type="text/markdown",  
    url="https://github.com/josetorraca/vfm_v2/tree/vfm-branch-lasap",  
    packages=find_packages(),  # Automatically find sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "pandas>=1.3.0",
        "hampel>=0.0.5",
    ],  # Dependencies defined directly here
)

