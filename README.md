# SQL Logger Handler

This log handler pushes log messages to queue.

## Requirements

`make requirements`

## Tests

It is necessary to have the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` keys as environment variables.

`make test`

Depends on:

* pytest

## Create new release

To generate a new release is necessary, run the python 2.7 (https://github.com/peritus/bumpversion/issues/41).

We use `bumpversion` to generate new releases, following the base
principles of [SEMVER](http://semver.org/).

Run this on the `master` branch 
-   Patch [ X.X.0 to X.X.1 ] :

        make release-patch

-   Minor [ X.0.X to X.1.X ] :

        make release-minor

-   Major [ 0.X.X to 1.X.X ] :

        make release-major


Upload to PyPI

    make packaging

Update `master` and push new tag release

    git push && git push --tags
>>>>>>> sqs logger handler implementation
