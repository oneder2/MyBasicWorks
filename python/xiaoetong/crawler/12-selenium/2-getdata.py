from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# create service object, arrange path of the driver
service = Service("/home/gellar/opt/chromedriver-linux64/chromedriver")
# create web object
web = webdriver.Chrome(service = service)
# open page baidu, no need to specify "get" or "post"
web.get("https://www.baidu.com")

# print(web.page_source)

# analyze data
"""
1- based on html, use xpath, bs4
2- by selenium build-in data analyze method
"""
# get tag data, operate on tag, 
# create web object

"""
# via tag id
# find
# input_tag = web.find_element(By.ID, 'kw')
# find all
input_tag = web.find_element(By.ID, 'kw')
input_tag.send_keys('python')
"""

"""
# via class
tag = web.find_element(By.CLASS_NAME, 's_ipt')
tag.send_keys('python')
"""

"""
# via name
tag = web.find_element(By.NAME, 'wd')
tag.send_keys('python')
"""

"""
#via name of tah(first one only)
# if want to find all, use find_element
web.find_element(BY.TAG.NAME, "input")
tag.send_keys("python1")
"""

"""
# via xpath
#//input[@id="kw"]
tag = web.find_element(By.XPATH, '//input[@id="kw"]')
tag.send_keys('python')
"""

# via css
#id = kw #kw
tag = web.find_element(By.CSS_SELECTOR, '#kw')
tag.send_keys('python')

# edit window
# maximize
# web.maximize_window()




