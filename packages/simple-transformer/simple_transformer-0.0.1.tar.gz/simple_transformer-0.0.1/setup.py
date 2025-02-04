from setuptools import setup, find_packages

setup(
    name="simple-transformer",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch",
    ],
    include_package_data=True,
    description="A simple and modular implementation of the Transformer model in PyTorch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Suryansh Shakya",
    author_email="suryanshsinghshakya1@gmail.com",
    url="https://github.com/nullHawk/simple-transformer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
