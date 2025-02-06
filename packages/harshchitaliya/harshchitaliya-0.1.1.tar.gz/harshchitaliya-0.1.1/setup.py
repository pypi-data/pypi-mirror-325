from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="harshchitaliya",
    version="0.1.1",
    author="Harsh Chitaliya",
    author_email="harshchitaliya193@example.com",
    description="Text Manipulation and Analysis Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshchi19/harsh",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
