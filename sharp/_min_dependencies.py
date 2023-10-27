"""All minimum dependencies for sharp."""
import argparse

NUMPY_MIN_VERSION = "1.20.0"
PANDAS_MIN_VERSION = "1.3.5"
MATPLOTLIB_MIN_VERSION = "2.2.3"

# The values are (version_spec, comma separated tags)
dependent_packages = {
    "numpy": (NUMPY_MIN_VERSION, "install"),
    "pandas": (PANDAS_MIN_VERSION, "install"),
    "matplotlib": (MATPLOTLIB_MIN_VERSION, "optional"),
    #  "ml-research": ("0.4.2", "optional"),
    "pytest-cov": ("3.0.0", "tests"),
    "flake8": ("3.8.2", "tests"),
    "black": ("22.3", "tests"),
    "pylint": ("2.12.2", "tests"),
    "mypy": ("1.6.1", "tests"),
    "types-requests": ("2.31.0.10", "tests"),
    "coverage": ("6.2", "tests"),
    "sphinx": ("4.2.0", "docs"),
    "numpydoc": ("1.0.0", "docs, tests"),
    #  "sphinx-material": ("0.0.35", "docs"),
    #  "nbsphinx": ("0.8.7", "docs"),
    #  "recommonmark": ("0.7.1", "docs"),
    #  "sphinx-markdown-tables": ("0.0.15", "docs"),
    #  "sphinx-copybutton": ("0.4.0", "docs"),
}


# create inverse mapping for setuptools
tag_to_packages: dict = {
    extra: [] for extra in ["install", "optional", "docs", "examples", "tests", "all"]
}
for package, (min_version, extras) in dependent_packages.items():
    for extra in extras.split(", "):
        tag_to_packages[extra].append("{}>={}".format(package, min_version))
    tag_to_packages["all"].append("{}>={}".format(package, min_version))


# Used by CI to get the min dependencies
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get min dependencies for a package")

    parser.add_argument("package", choices=dependent_packages)
    args = parser.parse_args()
    min_version = dependent_packages[args.package][0]
    print(min_version)
