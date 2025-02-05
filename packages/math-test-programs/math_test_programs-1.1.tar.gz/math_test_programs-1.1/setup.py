from setuptools import setup, find_packages

setup(
    name="math_test_programs",  # Your package name
    version="1.1",              # Version number
    packages=find_packages(),   # Automatically find packages
    description="A collection of 13 Python programs for math-related tasks",
    long_description=open('README.md').read(),  # Optional: Readme content
    long_description_content_type="text/markdown",
    author="Sachethan",

    url="https://github.com/yourusername/math-test-programs",  # Optional: Your GitHub repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
