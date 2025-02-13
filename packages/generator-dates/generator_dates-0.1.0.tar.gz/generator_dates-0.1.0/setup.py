from setuptools import setup, find_packages

setup(
    name="generator_dates",
    version="0.1.0",
    description="A Python package to generate random dates in different formats and languages.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Misha",
    author_email="bobyyy239@gmail.com",
    url="https://github.com/Triram-2/generator_dates",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
