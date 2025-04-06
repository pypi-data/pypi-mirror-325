from setuptools import setup, find_packages

setup(
    name="user-management",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Brennen",
    author_email="brennen.barney@gmail.com",
    description="A user management package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clickstack/user-management",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 