from setuptools import setup, find_packages

setup(
    name='GestUniDt',
    version='1.0.3',
    description='A Python library quickly store and fetch different types of data.',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    author='eaannist',
    author_email='eaannist@gmail.com',
    url='https://github.com/eaannist/GestUniDt',
    packages=find_packages(),
    install_requires=['pandas'],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
