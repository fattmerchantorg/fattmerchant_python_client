import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fattmerchant",
    version="1.1.9",
    author="Fattmerchant INC",
    author_email="support@fattmerchant.com",
    description="Python Client for Fattmerchant's Omni API",
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
