from setuptools import setup, find_packages

setup(
    name="ncep_data_req",
    version="0.1.1",
    author="Subhrajit Rath",
    author_email="you@example.com",
    description="Download and process NCEP GFS 0.25° data via ASCII interface",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "xarray",
        "requests",
        "matplotlib",
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
