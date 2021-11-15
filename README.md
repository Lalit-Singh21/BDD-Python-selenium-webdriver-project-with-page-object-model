# Set up

We'll need a few things to install:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate
or in windows
source venv/Scripts/activate
cd C:/Users/../Selenium tests
python -m behave tests/acceptance
```
##To create virtual env:
```bash
>virtualenv --python python3.10 venv    (python3.10 or full path to python exe)
>venv/Scripts/activate
```

##To create correct chrome driver:
For automatically installing and managing webdriver without worrying setting paths and copying binary 

```
cli:
pip install webdriver-manager

Code:
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

```