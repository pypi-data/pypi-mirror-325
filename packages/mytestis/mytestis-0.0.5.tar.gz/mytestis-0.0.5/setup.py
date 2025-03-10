from setuptools import setup, find_packages

setup(
    name="mytestis",
    version="0.0.5",
    packages=find_packages(),
    install_requires=[
        # "clight",
        
    ],
    entry_points={
        "console_scripts": [
            "mytestis=mytestis.main:main",  # Entry point of the app
        ],
    },
    package_data={
        "mytestis": [
            "main.py",
            "__init__.py",
            ".system/imports.py",
            ".system/index.py",
            ".system/modules/jobs.py",
            ".system/sources/clight.json",
            ".system/sources/logo.ico"
        ],
    },
    include_package_data=True,
    author="Irakli Gzirishvili",
    author_email="gziraklirex@gmail.com",
    description="Test Description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)
