from setuptools import setup, find_packages

setup(
    name="pdf_string_search",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to search for strings in multiple PDF files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pdf_string_search",
    packages=find_packages(),
    install_requires=[
        "pymupdf"
    ],
    entry_points={
        "console_scripts": [
            "pdf-search=pdf_string_search.main:main"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)