from setuptools import setup, find_packages

setup(
    name="bihelp_development",
    version="1.0.0",
    description="BigQuery deployment tool with environment substitution",
    author="David Macák",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "bihelp=bihelp.bihelp:main",
        ],
    },
    python_requires=">=3.10",
)