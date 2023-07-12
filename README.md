# Unit Test Example

This simple program implements the Fibonacci sequence and tests for it.

## Installation

Ensure pipenv is properly installed.

```bash
pipenv sync
```

## Execution

First activate the virtual environment

```bash
pipenv shell
```

Now run the following to run pytest in verbose mode with coverage, and then view the report.

```bash
coverage run -m pytest -v && coverage report
```

Output:
```shell
====================================================================== test session starts =======================================================================
platform linux -- Python 3.11.2, pytest-7.4.0, pluggy-1.2.0 -- /home/james/.local/share/virtualenvs/utest_eg0-hiS3p3rU/bin/python
cachedir: .pytest_cache
rootdir: /home/james/projects/2023/python/utest_eg0
plugins: cov-4.1.0
collected 3 items                                                                                                                                                

tests/test_fib_lim.py::test_upper_limit PASSED                                                                                                             [ 33%]
tests/test_fib_lim.py::test_lower_limit PASSED                                                                                                             [ 66%]
tests/test_fib_lim.py::test_values PASSED                                                                                                                  [100%]

======================================================================= 3 passed in 0.04s ========================================================================
Name                    Stmts   Miss  Cover
-------------------------------------------
fib.py                      7      0   100%
tests/__init__.py           0      0   100%
tests/test_fib_lim.py      15      0   100%
-------------------------------------------
TOTAL                      22      0   100%

```