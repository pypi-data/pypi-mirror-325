## SpecStory

## Untitled (07/02/2025, 12:41:17)

_**User**_

i want to release and publish new version

---

_**Assistant**_

Let me help you publish a new version of your package. First, I'll check the project structure and configuration to determine the best approach.

<thinking>
1. Core requirement: Release and publish a new version of the Python package

2. Implementation approaches:
- Manual version bump + build + publish to PyPI
- Using automated release tools like poetry/twine
- Using CI/CD pipeline if configured

3. Based on the files, I see pyproject.toml exists, suggesting this is a Poetry project.
This is the simplest and most maintainable approach.

4. Verification:
- Need to check current version
- Ensure tests pass
- Build package
- Publish to PyPI
</thinking>

Let me first check your project configuration.

---

_****_

Read file: pyproject.toml

---

_****_



I see this is a Python package using Hatch as the build system. Let's first run the tests to ensure everything is working correctly before publishing.

---

_****_



---

_****_



---



---

