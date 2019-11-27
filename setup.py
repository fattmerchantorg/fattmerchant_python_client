import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fattmerchant",
    version="2.0.0",
    author="Fattmerchant INC",
    author_email="support@fattmerchant.com",
    description="Python 3.x Client for Fattmerchant's Omni API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fattmerchantorg/fattmerchant_python_client",
    packages=setuptools.find_packages(),
    package_data={
        "": ["*.config", "*.txt"],
    },
    install_requires=["ddt", "requests"],
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
