from setuptools import setup, find_packages

setup(
    name="my_python_programs",  # Name of your package
    version="0.1",  # Version of your package
    packages=find_packages(),  # Automatically discover all packages
    install_requires=[  # Add any dependencies here
        # "numpy", "matplotlib", etc.
    ],
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type='text/markdown',  # Use markdown for long description
    classifiers=[
        "Programming Language :: Python :: 3",  # Python version compatibility
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum required Python version
)
