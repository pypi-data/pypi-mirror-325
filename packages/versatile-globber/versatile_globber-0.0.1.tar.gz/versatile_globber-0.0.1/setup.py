from setuptools import setup, find_packages

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="versatile_globber",
    version="0.0.1",
    description="This versatile globber helps developers easily look for file that matches any extensions within many folders.",
    package_dir={"" : "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hùng Cường",
    author_email="cuongdayne17@gmail.com",
    license="MIT",
    url="https://github.com/ticuong78/versatile_globber",
    python_requires=">=3.13",
    extras_require={
        "dev": ["twine>=6.0.0"]
    }
)