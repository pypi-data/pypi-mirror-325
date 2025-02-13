from test_pypi_project import hello

def test_hello():
    assert hello() == "Hello, PyPI!"