from setuptools import setup, find_packages
from pathlib import Path


setup(
    name="sms_spam_detection",
    version="0.1.4",
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    include_package_data=True,
)
