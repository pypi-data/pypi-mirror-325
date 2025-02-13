from setuptools import setup, find_packages

setup(
  name="arnelify_server",
  version="0.6.0",
  author="Arnelify",
  description="Minimalistic dynamic library which is a powerful http-server written in C and C++.",
  url='https://github.com/arnelify/arnelify-server-python',
  packages=find_packages(),
  install_requires=[],
  long_description=open("README.md", "r", encoding="utf-8").read(),
  long_description_content_type="text/markdown",
  classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
  ]
)