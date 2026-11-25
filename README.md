# Stepik Selenium and Python exercises

The final Page Object project covers the storefront's login page, product details and basket. The language and file upload exercises are included as separate test modules.

Install Python, Google Chrome and the dependencies. Run the four scenarios for peer review:

    python -m pip install -r requirements.txt
    python -m pytest -v --tb=line --language=en -m need_review

To see the French button label, run `python -m pytest -s --language=fr test_items.py`. Use `--headless` to run Chrome without a window. Each test starts with a fresh browser session. The offer 7 scenario is marked as an expected failure because the product name in the success message changes.
