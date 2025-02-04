from setuptools import setup, find_packages

setup(
    name='bodma',  # Name of your package
    version='0.1.0',  # Version of your package
    packages=find_packages(),
    install_requires=[],  # Add dependencies if needed
    author='Your Name',
    author_email='sunilsingh18061995@gmail.com',
    description='A library for mathematical operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/bodma',  # Add your GitHub link or project page
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify minimum Python version
)
