from setuptools import setup, find_packages

setup(
    name="csmxnet",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "cryptography"
    ],
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="AI-proof, post-quantum secure networking library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/csmxnet",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
