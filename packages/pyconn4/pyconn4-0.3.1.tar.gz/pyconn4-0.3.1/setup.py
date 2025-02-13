from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="pyconn4",
    version="0.3.1",
    description="python connection tools collection",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="James Liu",
    author_email="liuchuanbo@gmail.com",
    url="",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=["qPython4==0.1.0", "numpy==2.0.2", "pandas==2.2.2"],
)
