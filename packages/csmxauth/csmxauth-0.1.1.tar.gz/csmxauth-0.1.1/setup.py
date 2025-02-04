from setuptools import setup, find_packages

setup(
    name="csmxauth",  # PyPI package name
    version="0.1.1",  # Increment this version for new updates
    description="Post-Quantum Secure Authentication Library",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    url="https://github.com/Sumedh1599/csmxauth",  # Change to your actual repo link
    packages=find_packages(),  # Auto-detects `csmxauth` package
    install_requires=[
        "cryptography",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.7",
)
