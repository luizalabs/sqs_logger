export PYTHONPATH=$PYTHONPATH:$(pwd)

#SQS
export QUEUE_NAME=sqs-logger
export REGION_NAME=us-east-1

#Credentials
export AWS_ACCESS_KEY_ID=AKIAJI5SNLMVL5DFW6KA
export AWS_SECRET_ACCESS_KEY=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

test-integration:
	@py.test -rxs --pdb -k$(Q) sqs_logger -m 'integration'

requirements:
	@pip install -r requirements/base.txt --upgrade

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major

packaging:
	python setup.py sdist bdist_wheel upload -r pypicloud
