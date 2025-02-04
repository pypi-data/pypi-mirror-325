from setuptools import setup, find_packages

setup(
    name="gpp-cracker",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pycryptodome",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "gpp-cracker = gpp_cracker.cli:main"
        ]
    },
    author="Chowdhury Faizal Ahammed",
    description="A tool to decrypt GPP passwords",
    license="MIT",
)
