export PYTHONPATH=$PYTHONPATH:$(pwd)

test:
	@py.test -vv -xs sqs_logger

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
	@flake8 . --exclude=.tox

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f coverage.xml
