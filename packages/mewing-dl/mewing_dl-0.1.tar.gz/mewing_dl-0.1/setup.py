# setup.py
from setuptools import setup, find_packages

setup(
    name="mewing_dl",
    version="0.1",
    packages=find_packages(),
    description="A simple library for displaying code and markdown tasks in Jupyter",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/scipit",  # при необходимости укажите репозиторий
    license="MIT",  # или другая лицензия
    install_requires=[
        "nbformat",
        "ipython",
        "setuptools"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
