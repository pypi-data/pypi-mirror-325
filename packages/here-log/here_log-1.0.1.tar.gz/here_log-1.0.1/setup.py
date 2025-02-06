from setuptools import setup, find_packages

setup(
    name='here_log',                            # The name of the package
    version='1.0.1',                        # Package version
    description='A package to print the current position in code',
    long_description=open('README.md').read(),  # Optional: long description from the README file
    long_description_content_type='text/markdown',
    author='Matt Werner',
    author_email='motomatt5040@gmail.com',
    url='https://github.com/MotoMatt5040/here',  # URL to the project repository
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
