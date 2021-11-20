# Set up

We'll need a few things to install:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):
behave.exe ".\tests\acceptance\content.feature" -t '@dockertest'


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

## running behave test from command line
## for single scenario
behave.exe ".\tests\acceptance\content.feature" -t '@BlogPageTitle'
#for multiple features
behave.exe ".\tests\acceptance\content.feature" ".\tests\acceptance\navigation.feature"

##run app and test from command line-- worked in kali linux:
/mnt/c//venv/Scripts/python.exe app.py & behave.exe ".\tests\acceptance\content.feature" -t '@HomePageTitle'


##docker commands
#standalone server hub and node config
docker run -d -p 4444:4444 selenium/standalone-chrome
##running images
docker run -d -p 4446:4444 --shm-size=2g selenium/standalone-chrome:3.141.59-20210929

docker run -d -p 4445:4444 --shm-size 2g selenium/standalone-firefox:3.141.59-20210929


docker ps
docker stop container_id
docker inspect container_id

-e NODE_MAX_INSTANCES=5 -e NODE_MAX_SESSION=5
##docker with vnc viewer config
Chrome:$ docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g selenium/standalone-chrome-debug:3.141.59-20210929

Firefox:$ docker run -d -p 4445:4444 -p 5901:5900 --shm-size 2g selenium/standalone-firefox-debug:3.141.59-20210929


# creating grid network and hub
:$  $docker network create grid
 docker network ls

create selenium hub:
$ docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub:3.141.59-20210929

create/add node in hub:
$ docker run -d --net grid -e HUB_HOST=selenium-hub -v /dev/shm:/dev/shm selenium/node-chrome:3.141.59-20210929
$ docker run -d --net grid -e HUB_HOST=selenium-hub -v /dev/shm:/dev/shm selenium/node-firefox:3.141.59-20210929

##running with different browser, from command line :
behave.exe ".\tests\acceptance\content.feature" -t '@dockertest' --define 'chrome'

##running on different browsers spawning parallel runs through testrunner
python .\testrunner.py -b "{'c':1,'f': 1}" -t dockertest -f .\tests\acceptance\content.feature



