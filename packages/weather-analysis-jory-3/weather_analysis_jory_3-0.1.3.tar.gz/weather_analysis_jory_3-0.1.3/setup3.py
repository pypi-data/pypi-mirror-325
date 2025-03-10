from setuptools import setup, find_packages

setup(
    name='weather-analysis-jory-3',
    version='0.1.3',
    description='A package for loading and analyzing weather data',
    author='Jory Pitts',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
