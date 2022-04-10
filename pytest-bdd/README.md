## Conventions for file structure:

Project Structure
Project structure for pytest-bdd is actually pretty flexible (since it is based on pytest), but the following conventions are recommended:

All test code should appear under a test directory named “tests”.
Feature files should be placed in a test subdirectory named “features”.
Step definition modules should be placed in a test subdirectory named “step_defs”.
conftest.py files should be located together with step definition modules.
Other names and hierarchies may be used. For example, large test suites can have feature-specific directories of features and step defs. pytest should be able to discover tests anywhere under the test directory.

[project root directory]
|‐‐ [product code packages]
|-- [test directories]
|   |-- features
|   |   `-- *.feature
|   `-- step_defs
|       |-- __init__.py
|       |-- conftest.py
|       `-- test_*.py
`-- [pytest.ini|tox.ini|setup.cfg]
