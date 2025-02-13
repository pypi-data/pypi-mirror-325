from setuptools import setup, find_packages

setup(
    name="pyworktree",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "install-libs=pyworktree.installer:main"
        ],
    },
    author="Your Name",
    description="A package to install selected Python libraries.",
    long_description=open("README.md", encoding="utf-8").read(),  # Fix Unicode error
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
