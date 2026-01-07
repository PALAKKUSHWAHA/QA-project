# QA Automation Framework — QA-project

Project: Enterprise-grade QA automation framework for a web-based business application.

Summary
-
End-to-end ownership of test automation: framework design, scripting, execution, reporting, and CI integration. The framework validates UI, API, and database behavior for a role-based application supporting form workflows, dashboards, and reporting.

My Role & Responsibilities
-
- Designed and implemented a Hybrid Automation Framework with Page Object Model (POM) for maintainability.
- Owned test scripting in Java/Python, test execution with TestNG/PyTest, and build/dependency management via Maven when applicable.
- Implemented reporting with Extent/Allure and integrated suites into Jenkins for CI execution.
- Wrote reusable utilities for browser handling, explicit waits, screenshots, logging, and environment-based configs.
- Performed database validations using SQL to assert backend state after UI/API actions.

Technology Stack
-
- UI Automation: Selenium WebDriver
```markdown
# QA Automation Framework — QA-project

Project: Enterprise-grade QA automation framework for a web-based business application.

Summary
-
End-to-end ownership of test automation: framework design, scripting, execution, reporting, and CI integration. The framework validates UI, API, and database behavior for a role-based application supporting form workflows, dashboards, and reporting.

My Role & Responsibilities
-
- Designed and implemented a Hybrid Automation Framework with Page Object Model (POM) for maintainability.
- Owned test scripting in Java/Python, test execution with TestNG/PyTest, and build/dependency management via Maven when applicable.
- Implemented reporting with Extent/Allure and integrated suites into Jenkins for CI execution.
- Wrote reusable utilities for browser handling, explicit waits, screenshots, logging, and environment-based configs.
- Performed database validations using SQL to assert backend state after UI/API actions.

Technology Stack
-
- UI Automation: Selenium WebDriver
- Languages: Java / Python
- Test Runners: TestNG / PyTest
- Build: Maven
- API Tools: Postman, REST Assured
- CI/CD: Jenkins (Git-based workflows)
- DB: SQL (validation queries)
- Reporting: Extent Reports, Allure
- VCS: Git

Framework Architecture
-
- Page Object Model (POM) for UI element encapsulation
- Data-driven testing using Excel/JSON for test inputs
- Reusable utilities: browser factory, wait helpers, screenshot capture, logger
- Environment configuration for QA/staging via centralized config files
- Centralized test runner that produces CI-friendly reports and artifacts

Test Coverage
-
- UI Scenarios: user registration/login, role-based access (Admin/User), form validations, end-to-end business workflows, dashboard data verification, cross-browser testing (Chrome, Firefox)
- API Scenarios: authentication/authorization, user CRUD, data submission/retrieval, status code checks, response validations, JSON schema checks, negative and boundary tests
- Database: SQL queries to verify persistence and data consistency after UI/API operations

CI/CD Integration
-
- Integrated test suites into Jenkins pipelines.
- Smoke tests run on every build; full regression executed nightly.
- Test reports and failure artifacts published to Jenkins and shared with stakeholders.

Defect Management
-
- Logged defects with clear reproduction steps, screenshots, and logs.
- Collaborated with developers for reproductions and retests; validated fixes through regression runs.

Results & Impact
-
- Reduced manual regression effort by ~60%.
- Improved release confidence and stability with faster feedback cycles.
- Early defect detection in CI pipelines improved product quality.

Next Steps (suggested)
-
- Add sample `tests/smoke` and `tests/regression` suites for the main business flows.
- Add a GitHub Actions / Jenkinsfile sample to demonstrate CI integration and artifact publishing.
- Provide contributor onboarding and test data setup guides.

How to run the provided UI smoke samples
-
- Prerequisites: Python 3.10+, Chrome (or Chrome-compatible) browser available for the driver to use.
- Install dependencies and run the Sauce Demo inventory test (headless by default):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/smoke/test_login_saucedemo.py -q
```

- Files added as examples:
	- `requirements.txt` — Python deps (pytest, selenium, webdriver-manager)
	- `pytest.ini` — pytest config
	- `Jenkinsfile` — sample Jenkins pipeline to run smoke tests
	- `tests/smoke/test_healthcheck.py` — placeholder API health check
	- `tests/smoke/test_ui_smoke.py` — minimal Selenium smoke placeholder
	- `tests/smoke/test_login_smoke.py` — generic login smoke using `LoginPage`
	- `tests/smoke/test_login_saucedemo.py` — concrete Sauce Demo login smoke
	- `tests/smoke/test_inventory_after_login.py` — inventory validation after login
	- `framework/pages/login_page.py` — generic LoginPage POM
	- `framework/pages/sauce_login_page.py` — Sauce Demo POM
	- `framework/pages/inventory_page.py` — Inventory POM

Notes
-
- CI runners often require a browser binary or a browser-enabled runner (self-hosted or Docker). If CI fails to start a browser, consider using a Selenium standalone container or a headless browser image.

Contact
-
Open an issue or pull request for questions or contributions.

```
