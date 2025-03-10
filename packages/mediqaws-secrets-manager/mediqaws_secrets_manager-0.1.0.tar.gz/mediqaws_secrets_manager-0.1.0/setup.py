from setuptools import setup, find_packages

with open("README.md", "r") as fp:
  long_description = fp.read()

setup(
  name="mediqaws-secrets-manager",
  version="0.1.0",
  author="Smartmediq",
  author_email="dev@smartmediq.com",
  description="AWS Secrets Manager with caching",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/SmartMediQ/mediqaws-secrets-manager",
  packages=find_packages(
    exclude=["tests", "tests.*"],
  ),
  classifiers=[
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  python_requires=">=3.9",
  install_requires=[
    "boto3",
  ],
)
