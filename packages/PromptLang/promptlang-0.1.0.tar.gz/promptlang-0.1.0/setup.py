from setuptools import setup, find_packages

setup(
    name="PromptLang",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Md Injemamul Irshad",
    author_email="injemam.irshad@gmail.com",
    description="A lightweight language for dynamic prompt processing with inline data transformations and caching.",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/injemamul/PromptLang",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
