# mutwo.ext-example

This is an example for a [mutwo](https://github.com/mutwo-org/mutwo) extension package.

## Making your own extension package

For making your own extension, you can clone this package:

```sh
git clone https://github.com/mutwo-org/mutwo.ext-example
```

Next edit the `setup.py` file and replace

1. `name="mutwo.ext-example"` with your extensions name
2. `description="example extension for event based framework for generative art"` with a description for your extension
3. `url="https://github.com/mutwo-org/mutwo.ext-example"` with your project url

Don't forget to change the `author` and `author_email` arguments.
Remove the hidden `.git` directory and make a new git project and upload it.

## Running tests

You can use the `run_tests.sh` bash script, which will create a virtual environment at the `/tmp` directory where the tests will be executed.

```sh
bash run_tests.sh
```

## Adding continuous integration / continuous deployment via [circleci](https://circleci.com)

There is already a default circleci config file at `.circleci/config.yml`.
Make an account at `circleci` if you don't have any yet.
Under `projects` select your new project and add a pipeline.
If you want to publish your package at [pypi](pypi.org/) you have to add the environment variables:

- TWINE_USERNAME
- TWINE_PASSWORD

with the user name and password for your [pypi](pypi.org/) account.
If you don't want to publish your package at pypi remove the `pypi_publish` job from the circleci config file.
