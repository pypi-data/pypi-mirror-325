from setuptools import setup, find_packages

setup(
    name='apectoolpy',
    version='0.1',
    description='A Python package for probabilistic seismic hazard analysis (PSHA)',
    author='Albert Pamonag',
    author_email='albert@apeconsultancy.net',
    url='https://github.com/albertp16/apec-py',
    packages=find_packages(),
    install_requires=[
        # Add required dependencies here, e.g., 'numpy', 'pandas', etc.
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    company='Albert Pamonag Engineering Consultancy',
)