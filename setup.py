from setuptools import setup

setup_options = dict(
    name='sqs_logger',
    version='1.0.3',
    description='',
    author='Luiz Gois',
    author_email='luiz.gois@luizalabs.com',
    url='https://github.com/luizalabs/sqs_logger',
    license="MIT License",
    keywords='sqs logging',
    packages=[
        'sqs_logger',
        'sqs_logger.aws'
    ]
)

setup(**setup_options)
