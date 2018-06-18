from setuptools import setup, find_packages

download_url = 'https://github.com/DanielBacci/custom_fields/tarball/master'

with open('requirements/base.txt') as requirements_file:
    requirements_file = requirements_file.readlines()

REQUIREMENTS = [
    requirement for requirement in requirements_file
    if not requirement.startswith('-')
]

setup(
    name='custom_fields',
    version='0.0.1',
    install_requires=REQUIREMENTS,
    url='https://github.com/DanielBacci/custom_fields',
    author='Daniel Bacci',
    author_email='danielhdbacci@gmail.com',
    keywords='Django cpf cnpj validate form',
    packages=find_packages(exclude=['tests*']),
    description=(
        'Python module for brazilian validate CPF and CNPJ for Django.'
    ),
    long_description=(
        'Use in a project Django for validate CPF and CNPJ'
    ),
    download_url=download_url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
