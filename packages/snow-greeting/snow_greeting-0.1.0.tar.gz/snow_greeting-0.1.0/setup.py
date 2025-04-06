# setup.py
from setuptools import setup, find_packages

setup(
    name='snow_greeting',
    version='0.1.0',
    description='A package that prints a snowy greeting message.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='oracle1993',
    author_email='dragonknight.work.1993@gmail.com',
    url='https://github.com/oracle1993/greetings_snow',  # Replace with your actual URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
