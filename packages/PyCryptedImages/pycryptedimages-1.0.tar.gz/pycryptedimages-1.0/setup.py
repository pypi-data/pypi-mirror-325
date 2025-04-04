from setuptools import setup, find_packages

setup(
    name='PyCryptedImages',  # Your package name
    version='1.0',  # Initial version
    description='A Python package to hide text in fake image files',  # Short description
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type='text/markdown',  # Content type for README
    author='Roshan D Roy',  # Your name
    author_email='roshandeepuroy@gmail.com',  # Your email address
    url='https://github.com/yourusername/PyCryptedImages',  # Link to the package repository
    packages=find_packages(),  # Automatically find packages in the source folder
    classifiers=[  # Classifiers help users find your package
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',  # OSI-approved MIT License
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[  # List of dependencies
        # Example: 'numpy', 'pygame', etc.
    ],
)
