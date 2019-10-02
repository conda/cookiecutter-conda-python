import pytest


@pytest.fixture
def context():
    """Test template creation with test parameters."""
    return {
        "full_name": "test name",
        "email": "test@email.com",
        "github_username": "test_username",
        "repo_name": "test_repo",
        "package_name": "test_repo",
        "project_short_description": "Test description.",
        "version": "0.1.0",
    }


def test_template(cookies, context):
    """Test the template for proper creation.

    cookies is a fixture provided by the pytest-cookies
    plugin. Its bake() method creates a temporary directory
    and installs the cookiecutter template into that directory.
    """
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_repo'
    assert result.project.isdir()


def test_has_license(cookies, context):
    context["open_source_license"] = "BSD"
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.join('LICENSE').check(file=1)

def test_no_license(cookies, context):
    context["open_source_license"] = "Proprietary"
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert not result.project.join('LICENSE').check(file=1)


def test_no_noarch(cookies, context):
    context["noarch_python"] = "n"
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    with result.project.join('conda.recipe','meta.yaml').open() as f:
        recipe = f.read()
        assert "noarch: python" not in recipe


def test_no_cli(cookies, context):
    context["include_cli"] = "n"
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    with result.project.join('conda.recipe','meta.yaml').open() as f:
        recipe = f.read()
        assert "entry_points" not in recipe
    with result.project.join('setup.py').open() as f:
        setup = f.read()
        assert "entry_points" not in setup
    assert not result.project.join('tests/test_cli.py').check(file=1)
    basename = result.project.basename
    assert not result.project.join(basename, 'cli.py').check(file=1)
    assert not result.project.join(basename, '__main__.py').check(file=1)
