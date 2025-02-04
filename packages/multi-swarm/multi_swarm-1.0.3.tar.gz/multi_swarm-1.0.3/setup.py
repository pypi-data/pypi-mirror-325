from setuptools import setup, find_packages

setup(
    name="multi-swarm",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "google-generativeai",
        "pytest",
        "pytest-cov",
        "pytest-mock",
    ],
) 