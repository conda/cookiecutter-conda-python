#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.open_source_license }}' == 'Proprietary':
        remove_file('LICENSE')

    if '{{ cookiecutter.include_cli }}' != 'y':
        remove_file('src/{{ cookiecutter.package_name }}/__main__.py')
        remove_file('src/{{ cookiecutter.package_name }}/cli.py')
        remove_file('tests/test_cli.py')
