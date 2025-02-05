from setuptools import setup, find_packages

setup(
    name="txt-reader",
    version="0.1.0.3",
    packages=find_packages(),
    install_requires=[],
    author="mistertayodimon",
    author_email="",
    description="Простая библиотека на Python которая работает с TXT",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/txt-reader/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)