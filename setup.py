import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fattmerchant",
    version="1.1.2",
    author="Austin Burns",
    author_email="austin.burns@fattmerchant.com",
    description="Python client for Fattmerchant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fattmerchantorg/fattmerchant_python_client",
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.config", "*.txt"],
    },
    install_requires=["ddt", "requests"],
    python_requires='>=2.7',
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
