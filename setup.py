import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('requirements/prod.txt') as requirements_file:
    requirements_file = requirements_file.readlines()


DEPENDENCY_LINKS = [
    link.split()[1] for link in requirements_file
    if link.startswith('-')
]

REQUIREMENTS = [
    requirement for requirement in requirements_file
    if not requirement.startswith('-')
]

for link in DEPENDENCY_LINKS:
    match = re.search('/(\w+).git', link)
    if match:
        REQUIREMENTS.append(match.group(1))

setup_options = dict(
    name='sqs_logger',
    version='1.0.1',
    description='',
    author='Luiz Gois',
    author_email='luiz.gois@luizalabs.com',
    url='https://github.com/luizalabs/sqs_logger',
    license="MIT License",
    keywords='sqs logging',
    packages=[
        'sqs_logger',
        'sqs_logger.aws'
    ],
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCY_LINKS,
)

setup(**setup_options)
