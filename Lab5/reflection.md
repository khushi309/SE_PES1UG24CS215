# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and style violations before the software is deployed.

## 2. What did Pylint help identify?

Pylint identified code-quality issues such as missing docstrings, inconsistent naming, unused imports, and problematic programming practices. Fixing these issues improved readability and maintainability. The final Pylint score was 10.00/10.

## 3. What did Bandit help identify?

Bandit identified potential security risks, including a hardcoded password, use of assert for validation, insecure temporary-file creation, and shell-command execution. These findings helped improve the security of the program. The final Bandit report identified no issues.

## 4. What did Flake8 help identify?

Flake8 identified formatting problems such as long lines, excessive blank lines, missing whitespace, and trailing whitespace. Correcting these problems made the code more consistent and readable. The final Flake8 run reported no violations.

## 5. Why is static code analysis important?

Static analysis can identify problems early, before they cause failures or security incidents. It encourages consistent coding practices, improves maintainability, and reduces the effort needed for debugging.

## 6. What did I learn from this lab?

I learned how to use Pylint, Bandit, and Flake8 to evaluate Python code quality, security, and formatting. I also learned to interpret reports, prioritize issues, correct the code, and rerun the tools to verify the changes.
