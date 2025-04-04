from setuptools import setup, find_packages

setup(
    name="regex-ease",
    version="0.1.0",
    description="A simple regex library to make your life easy :)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Siddesh Shewde",
    author_email="siddesh.shewde@gmail.com",
    url="https://github.com/Collaborative-Open-Source-Projects",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)