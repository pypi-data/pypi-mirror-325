from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="auto_translate",
    version="1.5",
    packages=find_packages(),
    install_requires=["deep_translator", "langdetect"],
    description="A simple automatic translation library",
    author="v4d6",
    author_email="",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
