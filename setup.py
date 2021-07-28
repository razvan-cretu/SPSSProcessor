import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SPSSProcessor",
    version="0.1.0",
    author="Cretu Razvan",
    author_email="razvan.cretu@dynatacorp.com",
    description="A helper module to enable Dynatas' DPs to process SPSS (sav) files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razvan-cretu/SPSSProcessor",
    project_urls={
        "Bug Tracker": "https://github.com/razvan-cretu/SPSSProcessor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)