from setuptools import find_packages, setup

setup(
    name="motti",
    version="0.0.43",
    author="lup1n",
    author_email="780966523@qq.com",
    description="some util functions",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pillow",
        "matplotlib",
        "pybase64",
        "pyyaml",
    ],
)