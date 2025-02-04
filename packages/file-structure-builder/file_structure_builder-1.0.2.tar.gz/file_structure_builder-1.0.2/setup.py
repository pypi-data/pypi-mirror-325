from setuptools import setup, find_packages

setup(
    name="file-structure-builder",
    version="1.0.2",
    author="aliasghar mirshahi",
    author_email="aliasgharmirshahi2004@gmail.com",
    description="A CLI tool to build file structures",
    packages=find_packages(),
    install_requires=[],  # Add dependencies from requirements.txt if needed
    entry_points={
        "console_scripts": [
            "fsb=file_structure_builder.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
