
from setuptools import setup, find_packages

setup(
    name="tiktaknawaf",
    version="1.0.1",
    author="Nawaf",
    author_email="your_email@example.com",
    description="A powerful TikTok video downloader",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tiktaknawaf",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
