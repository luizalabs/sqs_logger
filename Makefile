export PYTHONPATH=$PYTHONPATH:$(pwd)

#SQS
export QUEUE_NAME=sqs-logger
export REGION_NAME=us-east-1

test:
	@py.test -rxs --pdb -k$(Q) sqs_logger

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major

packaging:
	python setup.py sdist bdist_wheel upload -r pypicloud

lint:
	@isort --check
	@flake8

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f coverage.xml
