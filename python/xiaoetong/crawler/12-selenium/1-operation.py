from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import requests


# create service object, arrange path of the driver
service = Service("/home/gellar/opt/chromedriver-linux64/chromedriver")
# create web object
web = webdriver.Chrome(service = service)
# open page baidu, no need to specify "get" or "post"
web.get("https://www.baidu.com")

# edit window
# maximize
web.maximize_window()
# minimize
# web.minimize_window()

input()
