from setuptools import setup, find_packages

setup(
    name='complycat',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your library dependencies here
    ],
    entry_points={
        'console_scripts': [
            'complycat=complycat.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='An open-source Python library for regulatory compliance in the financial sector.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/3wilsoneric/complycat',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

# The setup.py file is a standard way to specify the metadata for your Python package. Let's break down the key components: 
# name: This is the name of your package on PyPI. You've named it 'complycat.'
# version: Specifies the version number of your package.
# packages: find_packages() automatically discovers and includes all Python packages in the project. This ensures that your library code is included during installation.
# install_requires: You can list dependencies required by your library here. Users will need these dependencies to use your library.
# entry_points: This section is for specifying entry points. In this example, it creates a console script named 'complycat' that points to the main function in the complycat package.
# author: Your name.
# author_email: Your email address.
# description: A short description of your library.
# long_description: Points to the contents of the README file, providing a more detailed description of your library. Make sure your README.md is present in the project.
# long_description_content_type: Specifies that the long description is in Markdown format.
# url: The URL of your project's homepage, often the GitHub repository
# classifiers: These are Trove classifiers, which help categorize your project. For example, it indicates the supported Python version, license, and operating system.
# Once you've created this file, it's used by tools like setuptools and pip during the packaging and distribution process. When users install your library using pip install complycat, these details help ensure a smooth installation.
