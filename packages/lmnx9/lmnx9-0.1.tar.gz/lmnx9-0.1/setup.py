from setuptools import setup, find_packages

setup(
    name="lmnx9",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="Limon Hossain",
    author_email="lmnx9johny@gmail.com",
    description="A simple HTTP library like requests by lmnx9",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LMNx9-JOHNY/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
