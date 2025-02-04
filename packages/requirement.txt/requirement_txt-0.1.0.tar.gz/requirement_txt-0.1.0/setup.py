from setuptools import setup, find_packages

setup(
    name='requirement.txt',
    version='0.1.0',
    author='Michelin CERT',
    author_email='maxime.escourbiac@michelin.com',
    description='',
    long_description_content_type='text/markdown',
    url='https://github.com/certmichelin/Waterhole',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)