from {{ cookiecutter.package_name }} import cli


def test_cli_template():
    assert cli.cli() is None
