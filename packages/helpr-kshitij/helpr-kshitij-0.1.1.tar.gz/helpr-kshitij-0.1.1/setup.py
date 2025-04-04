from setuptools import setup, find_packages

def read_file(file, default=""):
    """Read a file and return its contents, or return default if file is missing."""
    try:
        with open(file, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return default

# Read metadata files
long_description = read_file("README.rst", "A Python package to help you with your daily tasks")
version = read_file("VERSION", "0.1.0")
requirements = read_file("requirements.txt", "").splitlines()

setup(
    name="helpr-kshitij",
    version=version,
    author="Clinikally",
    author_email="kshitijsrivastava@clinikally.com",
    url="https://github.com/kshitijclinikally/testinghelpr",
    description="A Python package to help you with your daily tasks",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,  # Ensure additional files are included
    package_data={"": ["VERSION", "requirements.txt"]},  # Explicitly include files
)
