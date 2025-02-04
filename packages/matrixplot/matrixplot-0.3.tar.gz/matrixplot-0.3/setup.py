from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="matrixplot",
    version="0.3",
    py_modules=["matrixplot"],
    install_requires=["matplotlib"],
    description="📊 Conveniently plot matrices in matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["License :: OSI Approved :: MIT License"],
    license_file="MIT"
)
