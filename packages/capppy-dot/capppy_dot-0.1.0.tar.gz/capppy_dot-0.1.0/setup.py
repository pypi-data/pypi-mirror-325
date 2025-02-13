from setuptools import setup, find_packages

setup(
    name="capppy-dot",  # Nama package yang unik
    version="0.1.0",
    author="Alex Sirait",
    author_email="alexsirait1001@gmail.com",
    description="capppy-dot packaye cool!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
