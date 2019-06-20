import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fattmerchant",
    version="0.0.1",
    author="Tanmay Dutta",
    author_email="tanmay.datta86@gmail.com",
    description="python client for fattmerchant payment processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/fattmerchant",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)