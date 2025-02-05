from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="wqferr_image_processing",
    version="0.1.1",
    author="William Q Ferreira",
    author_email="wqferr@gmail.com",
    description="An example package wrapping simple functionality from skimage.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wqferr/trilha-python-dio-image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
