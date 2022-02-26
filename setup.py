import setuptools  # type: ignore

MAJOR, MINOR, PATCH = 0, 55, 0
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"
"""This project uses semantic versioning.
See https://semver.org/
Before MAJOR = 1, there is no promise for
backwards compatibility between minor versions.
"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extras_require = {"testing": ["nose", "coveralls"]}

setuptools.setup(
    name="mutwo.ext-example",
    version=VERSION,
    license="GPL",
    description="example extension for event based framework for generative art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AUTHOR_NAME",
    author_email="AUTHOR_EMAIL",
    url="https://github.com/mutwo-org/mutwo.ext-example",
    project_urls={"Documentation": "https://mutwo.readthedocs.io/en/latest/"},
    packages=[
        package
        for package in setuptools.find_namespace_packages(include=["mutwo.*"])
        if package[:5] != "tests"
    ],
    setup_requires=[],
    install_requires=[
        "mutwo.ext-core>=0.55.0, <0.56.0",
    ],
    extras_require=extras_require,
    python_requires=">=3.9, <4",
)
