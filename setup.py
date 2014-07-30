from distutils.core import setup
from setuptools import setup

setup(
    name='evplan',
    version='0.1.0',
    author='Abel Soares Siqueira',
    author_email='abel.s.siqueira@gmail.com',
    packages=['evplan'],
    package_data={'evplan': ['*/*.tmpl','*/*/*.tmpl']},
    url='https://github.com/abelsiqueira/evplan',
    license='LICENSE',
    description='A package and tool for creating conferences',
    long_description=open('README.md').read(),
    entry_points={'console_scripts': ['evplan = evplan.main:main']},
    data_files=[]
)
