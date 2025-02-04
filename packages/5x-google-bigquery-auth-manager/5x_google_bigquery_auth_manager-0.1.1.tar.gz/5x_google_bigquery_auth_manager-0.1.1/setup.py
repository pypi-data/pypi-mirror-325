from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="5x-google-bigquery-auth-manager",
    version="0.1.1",
    author="5X",
    author_email="support@5x.co",
    description="A simple Python library for creating a Google BigQuery client using either an access token or a service account JSON file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/5x-Platform/5x-nextgen-python-libraries.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
)