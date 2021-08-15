import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='latino',
    version='0.0.3',
    author="Daniele Lin",
    author_email="lindaniele25@gmail.com",
    license="MIT",
    description="Traduttore Latino: lemma, paradigma, grammatica e traduzione.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lindaniele",
    packages=setuptools.find_packages(),
    keywords=['latino', 'dizionario', 'olivetti', 'traduttore', 'latin', 'paradigma', 'traduzione'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'lxml',
        'bs4',
        'requests',
    ],
)