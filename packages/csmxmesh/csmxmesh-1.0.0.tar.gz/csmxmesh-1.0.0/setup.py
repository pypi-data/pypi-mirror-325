from setuptools import setup, find_packages
import os

setup(
    name="csmxmesh",
    version="1.0.0",
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="Next-Gen AI-Proof, Post-Quantum Secure Authentication System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/csmxmesh",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.8',
)

# PyPI Deployment Command
print("🚀 Building and Publishing csmxmesh to PyPI...")
