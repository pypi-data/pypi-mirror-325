from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tabotools",
    version="0.1.0",
    author="Maria",
    author_email="vpays.am@gmail.com",
    description="A data tools library for loading, preprocessing, exploratory analysis, and visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mariiavs/tabotools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "IPython",
    ],
)
