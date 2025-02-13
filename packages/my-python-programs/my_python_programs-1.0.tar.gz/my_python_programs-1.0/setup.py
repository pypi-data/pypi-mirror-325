from setuptools import setup, find_packages

setup(
    name="my_python_programs",  # Name of your package
    version="1.0",  # Package version (update this with each new release)
    packages=find_packages(),  # Automatically find all packages in the directory
    description="A collection of Python programs for various tasks",
    long_description=open('README.md').read(),  # If you have a README file, this will be the description
    long_description_content_type="text/markdown",  # If you're using Markdown in README
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    url="https://github.com/yourusername/my_python_programs",  # Replace with your GitHub repo or project URL
    classifiers=[  # Classifiers that provide information about the package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # You can replace this with your license type
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum required Python version
)
