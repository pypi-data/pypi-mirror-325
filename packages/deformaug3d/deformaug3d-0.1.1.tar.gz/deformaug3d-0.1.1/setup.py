from setuptools import setup, find_packages

setup(
    name="deformaug3d",
    version="0.1.1",
    author="Haifan Gong",
    author_email="haifangong@outlook.com",
    description="A package for 3D volume augmentation with configurable parameters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/haifangong/deformaug3d",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "torch",  # specify additional dependencies as needed
    ],
)


