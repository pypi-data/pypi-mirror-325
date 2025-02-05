from setuptools import setup, find_packages

setup(
    name="kleantext",
    version="0.1.4",
    author="Karan",
    author_email="Karansd00@gmail.com",
    description="A Python module for preprocessing text for NLP tasks",
    long_description=open("README.md", encoding="utf-8").read(),  # Fix Unicode error
    long_description_content_type="text/markdown",
    url="https://github.com/karan9970/kleantext",
    packages=find_packages(),
    install_requires=[
        "textblob>=0.15.3",
        "nltk>=3.7"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
     license="MIT"
)
