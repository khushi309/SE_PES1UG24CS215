# Lab 5: Static Code Analysis — Issue Log

## Project
Blood Donation Management System

## Tools Used
- Pylint: Code quality analysis
- Bandit: Security analysis
- Flake8: Python style and formatting analysis

## Issues Identified and Fixes

| No. | Issue | Tool | Original Location | Description | Fix Applied |
|---|---|---|---|---|---|
| 1 | Hardcoded password | Bandit | Line 5 | A password was stored directly in the source code. | Removed the hardcoded credential from the revised implementation. |
| 2 | Use of assert | Bandit | Line 18 | An assertion was used for input validation. | Replaced assertion-based validation with explicit validation logic. |
| 3 | Insecure temporary file | Bandit | Line 60 | tempfile.mktemp() can introduce security risks. | Used tempfile.NamedTemporaryFile() to create a temporary file securely. |
| 4 | Shell command execution | Bandit | Line 65 | os.system() executed a command through a shell. | Removed shell execution and replaced the helper with a safe notification-message function. |
| 5 | Mutable default argument | Pylint | Original registerDonor function | notes=[] could share a mutable list between function calls. | Used None as the default and initialized the list when needed. |
| 6 | Broad exception handling | Pylint | Original unitsFor function | except Exception caught errors too broadly. | Replaced broad exception handling with explicit input validation. |
| 7 | Naming and documentation issues | Pylint | Multiple locations | Function names did not follow snake_case, and docstrings were missing. | Improved naming consistency and added documentation strings. |
| 8 | Long line | Flake8 | Original line 7 | A line exceeded the recommended length. | Reformatted the code across multiple lines. |
| 9 | Excess blank lines | Flake8 | Original line 58 | Too many consecutive blank lines were present. | Removed unnecessary blank lines. |
| 10 | Inline comment spacing | Flake8 | Original line 80 | An inline comment lacked the required spacing. | Corrected comment spacing. |
| 11 | Missing operator whitespace | Flake8 | Original line 81 | An operator did not have appropriate surrounding whitespace. | Corrected operator spacing. |
| 12 | Trailing whitespace and final blank line | Flake8 | Revised file | Unnecessary whitespace and an extra blank line were detected. | Removed trailing whitespace and ensured exactly one final newline. |

## Verification

- Pylint final score: 10.00/10.
- Bandit final report: No issues identified.
- Flake8 final report: No style violations reported.

The before-and-after reports are retained in the project directory for comparison.
