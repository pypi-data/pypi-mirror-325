from setuptools import setup, find_packages

setup(
    name='bsdspy',
    version='0.1.5',
    description='This APEC internal use only for DPWH BSDS Standards',
    author='Albert Pamonag',
    author_email='albert@apeconsultancy.net',
    url='https://github.com/albertp16/apec-py',
    packages=find_packages(),
    install_requires=[
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    company='Albert Pamonag Engineering Consultancy',
)