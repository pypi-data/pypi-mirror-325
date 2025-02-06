from setuptools import setup, find_packages

setup(
    name="decentralised-signing-crypto-mock",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "cryptography>=3.4.7",
    ],
    author="Dave Butler",
    author_email="",
    description="A mocked first version of a signature library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 