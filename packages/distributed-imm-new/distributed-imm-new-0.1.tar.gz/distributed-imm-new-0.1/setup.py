import os
from setuptools import setup, find_packages

# Detect version directory, default to "version-1"
version_dir = os.getenv("IMM_VERSION", "version-1")

# Ensure the specified version directory exists
if not os.path.isdir(f"d-imm-python/{version_dir}"):
    raise ValueError(f"Specified version directory 'd-imm-python/{version_dir}' does not exist.")

setup(
    name="distributed-imm-new",
    version="0.1",
    description="A distributed implementation of the IMM algorithm for explaining clusters in Spark ML pipelines.",
    author="saadha",
    author_email="marium.20@cse.mrt.ac.lk",
    packages=find_packages(where=f"d-imm-python/{version_dir}"),
    package_dir={"": f"d-imm-python/{version_dir}"},
    install_requires=[
        "pyspark>=3.0.0",
        "scikit-learn",
        "pandas",
        "numpy",
        "graphviz",
        "cython"
    ],
    python_requires=">=3.6",
    include_package_data=True,
)