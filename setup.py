from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="first_test",
    version="0.0.3",
    author="Eduardo Tostes",
    author_email="eduardo.tostes.jf@gmail.com",
    description="Test Ping",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edkami/first_test",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)