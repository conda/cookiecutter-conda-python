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
        "version": "0.1.0"
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
