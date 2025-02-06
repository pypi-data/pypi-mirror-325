from setuptools import setup, find_packages

setup(
    name="goloce123",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="Thanh-Hung Chu",
    author_email="thanhhungchu95@gmail.com",
    description="A simple example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thanhhungchu95/goloce123",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
)
