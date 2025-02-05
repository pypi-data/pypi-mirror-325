from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nepali-normalizer",  # Ensure this matches your uploaded package name
    version="0.1.0",
    author="FancyCodeMaster",
    author_email="fancycodemaster@gmail.com",
    description="Advanced normalization toolkit for Nepali text processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FancyCodeMaster/nepali-normalizer",
    packages=find_packages(include=["nepali_normalizer", "nepali_normalizer.*"]),  # Explicitly find your package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'indic-nlp-library>=0.81',
        'regex',
    ],
)
