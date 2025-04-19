# How to Run

Below are the steps to run tests using `unittest` and `nose`:

1. **Run tests using `unittest`:**
    ```bash
    python3 -m unittest
    ```
    This command runs all the test cases in the current directory.

2. **Run tests with verbose output:**
    ```bash
    python3 -m unittest -v
    ```
    The `-v` flag provides detailed output for each test case.

3. **Install `nose` testing framework:**
    ```bash
    python3.8 -m pip install nose
    ```
    This installs the `nose` testing framework, which provides additional features for running tests.

4. **Run tests using `nose`:**
    ```bash
    nosetests -v
    ```
    The `-v` flag provides verbose output for the tests.

5. **Install `pinocchio` for better test output:**
    ```bash
    python3.8 -m pip install pinocchio
    ```
    The `pinocchio` package enhances the output of `nose` tests.

6. **Run tests with `pinocchio` enhancements:**
    ```bash
    nosetests --with-spec --spec-color
    ```
    The `--with-spec` and `--spec-color` options provide a more readable and colorful test output.

7. **Install `coverage` for code coverage reports:**
    ```bash
    python3.8 -m pip install coverage
    ```
    The `coverage` package is used to measure code coverage during testing.

8. **Run tests with code coverage:**
    ```bash
    nosetests --with-spec --spec-color --with-coverage
    ```
    This command runs the tests with enhanced output and generates a code coverage report.

9. **Generate a detailed coverage report:**
    ```bash
    coverage report -m
    ```
    The `-m` flag provides a detailed report showing which lines of code were missed during testing.

10. **Automating the parameters**
    ```bash
    [nosetests]
    verbosity=2
    with-spec=1
    spec-color=1
    with-coverage=1
    cover-erase=1
    cover-package=triangle

    [coverage:report]
    show_missing = True
    ```
    Create a new file named `setup.cfg` and paste these parameters.