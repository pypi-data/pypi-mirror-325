from setuptools import setup, find_packages

setup(
    name="harichselvamc",
    version="0.7.2",
    packages=find_packages(),
    description="A Python package to generate Pascal's Triangle and retrieve Wi-Fi passwords.",
    long_description="""
    A Python package that provides:
    1. Pascal's Triangle generation up to the specified number of rows.
    2. Cross-platform Wi-Fi password retrieval for Windows, macOS, and Linux. 

    Features:
    - Generate Pascal's Triangle easily.
    - Retrieve saved Wi-Fi passwords from system settings.
    - Works on Windows, macOS, and Linux.


    
    This package may be extended in future versions to include optimizations and additional functionality.
    """,
    long_description_content_type="text/plain",
    author="harichselvam",
    author_email="harichselvamc@gmail.com",
    url="https://github.com/harichselvamc/harichselvamc-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],  
    tests_require=["pytest"],
    test_suite="tests",
)
