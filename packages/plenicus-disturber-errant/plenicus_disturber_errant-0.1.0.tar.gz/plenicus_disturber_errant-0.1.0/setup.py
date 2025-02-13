from setuptools import setup, find_packages

setup(
    name="plenicus_disturber_errant",  # Unique package name
    version="0.1.0",
    author="Aderibigbe Ayomide",
    author_email="uniwylimp@gmail.com",
    description="A simple greeting package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(),
    install_requires=[],  # Dependencies (e.g., ["requests"])
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
