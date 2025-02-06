from setuptools import setup, find_packages

setup(
    name="AhmadYasin",  # Your library name
    version="1.1.1",  # Version number
    author="Ahmad Yasin",
    author_email="ahmadyasin.info@gmail.com",
    description="A helper library with useful functions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AhmadYasin1",  # GitHub URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
