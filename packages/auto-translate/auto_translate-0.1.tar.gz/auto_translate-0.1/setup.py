from setuptools import setup, find_packages

setup(
    name="auto_translate",
    version="0.1",
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
)
