from setuptools import setup, find_packages

setup(
    name="csmxauth",  # Package Name (Must be unique on PyPI)
    version="0.1.4",  
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="Post-Quantum Secure Authentication Library",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/csmxauth",  # Change to your GitHub repo
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "cryptography",  # Ensure dependencies are included
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
