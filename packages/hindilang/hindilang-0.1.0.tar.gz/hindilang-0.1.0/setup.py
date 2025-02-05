from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hindilang',
    version='0.1.0',
    author='Ujjwal Kumar Rajak',
    author_email='ujjwalrajak2002@gmail.com',
    description='A Hindi-language implementation',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Beasova-Corporation/Ilbpp.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)