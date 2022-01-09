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

## Adding new features

For adding new features it is the best if you adjust to mutwos internal structure and add them at the fitting submodule in [mutwo/ext](https://github.com/mutwo-org/mutwo.ext-example/tree/main/mutwo/ext).
More information regarding the scope of the single modules can be found at the docstrings of the `__init__.py` files in mutwos core module (for instance [here](https://github.com/mutwo-org/mutwo/blob/main/mutwo/core/events/__init__.py)).
If your provided functionality doesn't fit to any of the submodules scope it is best to first add a new submodule in [mutwos core package](https://github.com/mutwo-org/mutwo/tree/main/mutwo/core) and the respective boilerplate code in [mutwos ext package](https://github.com/mutwo-org/mutwo/tree/main/mutwo/ext).

## Adding and running tests

You can write tests using pythons buildin [unittest module](https://docs.python.org/3/library/unittest.html) inside the `tests` directory.
It may be best practice to repeat mutwos module structure inside the test directory (e.g. if you add a functionality in the `generators` package you should add a `package` directory inside the `tests` directory, where you will add the respective test files).
To run the tests you can use the `run_tests.sh` bash script, which will create a virtual environment at the `/tmp` directory where the tests will be executed.

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
