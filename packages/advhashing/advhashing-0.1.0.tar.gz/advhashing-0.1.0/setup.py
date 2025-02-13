from setuptools import setup, find_packages

setup(
    name="advhashing",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="Advanced cryptographic hashing library with salt, multi-threading, and HMAC authentication.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/advhashing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
