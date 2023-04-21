from distutils.core import setup
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="configura",
    packages=["configura"],
    version="0.1",
    license="MIT",
    description="Configura is a Python configuration library that enables you to convert a folder of .json files into an easily accessible configuration folder.",
    author="Philippe Mathew",
    author_email="philmattdev@gmail.com",
    url="",
    download_url="",
    keywords=["config"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
