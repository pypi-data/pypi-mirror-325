from setuptools import setup, find_packages # type: ignore

setup(
    name="securelib",
    version="1.0.1",
    description="A comprehensive security utility library for encryption, scanning, and vulnerability detection",
    author="Wada Kaede",
    author_email="kaede04079642@outlook.com",
    url="https://github.com/Wadakaede/secure_lib.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pycryptodome",
        "requests"
    ],
    python_requires='>=3.6',
)
