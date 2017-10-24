# cookiecutter-conda-python
A [cookiecutter](https://www.github.com/audreyr/cookiecutter "cookiecutter") template for 
conda packages using Python

## Features

  -  Ready-made conda recipe found in conda.recipe/meta.yaml
  -  Pre-configured .travis.yml for Travis CI
  -  Coverage report hosted on Coveralls

## Installation

Prior to installing cookiecutter-conda-python, the cookiecutter package must be installed in your environment. This is achieved via the following command::

    $ conda install cookiecutter

With cookiecutter installed, the cookiecutter-conda-python template can be installed with::

    $ cookiecutter https://github.com/conda/cookiecutter-conda-python.git

Once cookiecutter clones the template, you will be asked a series of questions related to your project::

    $ full_name [Full Name]: Enter your full name.

    $ email [Email Address]: Enter your email address.

    $ github_username [github_username]: Enter your github username.

    $ repo_name [repository_name]: Enter the name of your project's repository.

    $ package_name [package_name]: Enter the name of your package.

    $ application_name [application]: Enter the name of your GUI application.

    $ project_short_description [Short description]: Enter a short description about your project.

    $ version [0.1.0]: Enter the version number for your application.

## Usage

After answering the questions asked during installation, a conda Python package will be
created in your current working directory. This package will contain a simple CLI script
and the conda recipe necessary to build the application into a conda package.