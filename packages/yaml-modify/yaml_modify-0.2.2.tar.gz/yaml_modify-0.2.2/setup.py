from setuptools import setup, find_packages

setup(
    name="yaml_modify",
    version="0.2.2",
    packages=find_packages(),
    install_requires=["pyyaml", "argparse"],
    entry_points={
        "console_scripts": [
            "yamlmod=yaml_modify.main:main",
        ],
    },
    author="Dad Macintosh",
    author_email="gerano.03@mail.ru",
    description="A CLI tool for modifying YAML files, managing backups, and orchestrating test sequences.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/geonsonatt/yaml_modify",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)