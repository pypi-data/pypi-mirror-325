from setuptools import setup, find_packages
from pathlib import Path


# Read the README file for description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sms_spam_detection",
    version="0.1.6",
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    include_package_data=True,
    description="A Python package for SMS spam detection.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Required for proper formatting on PyPI
)
