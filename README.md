# Selenium language tests

Stepik course 575, lesson 3.6: a product page must contain one visible Add to basket button for every supported interface language.

Install Python, Google Chrome and the dependencies:

    python -m pip install -r requirements.txt
    pytest --language=es test_items.py
    pytest --language=fr test_items.py

The `browser` fixture sets Chrome's Accept-Language preference and closes the browser after each test.
