from setuptools import setup, find_packages

setup(
    name="pyprotodef",
    version="0.1.0",
    author="Amal v s",
    author_email="amal.vs.engineer@gmail.com",
    description="A lightweight binary protocol serialization library like ProtoDef but in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alchemist123/pyprotodef",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
