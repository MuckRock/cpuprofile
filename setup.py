import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cpuprofile",
    version="1.0.1",
    author="Dylan Freedman",
    author_email="freedmand@gmail.com",
    description="A simple Python package to profile CPU speed by computing the Fibonacci sequence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muckrock/cpuprofile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
