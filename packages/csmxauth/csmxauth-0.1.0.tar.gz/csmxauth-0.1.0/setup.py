from setuptools import setup, find_packages

setup(
    name="csmxauth",  # ✅ Change to your unique package name
    version="0.1.0",
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",  # ✅ Replace with your real email
    description="Post-Quantum Secure Authentication Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/csmxauth",  # ✅ Update if you have a GitHub repo
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
