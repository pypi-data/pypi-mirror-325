import setuptools

with open("README.md", "r", encoding="utf-8") as fh:  # For long description
    long_description = fh.read()

setuptools.setup(
    name="circle-area-opamV1.8",  # Your package name (must be unique on PyPI)
    version="0.1.0",  # Initial version
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple package to calculate circle area.",
    long_description=long_description,  # From README.md
    long_description_content_type="text/markdown", # Important for README.md
    url="https://github.com/yourusername/circle_area",  # Link to your repo (optional)
    packages=setuptools.find_packages(),  # Automatically find packages
    classifiers=[  # Metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Example License
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7', # Minimum Python version supported
)