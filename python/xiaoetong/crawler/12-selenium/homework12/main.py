from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re


# create service object, arrange path of the driver
service = Service("/home/gellar/opt/chromedriver-linux64/chromedriver")
# create web object
web = webdriver.Chrome(service = service)
# open page baidu, no need to specify "get" or "post"
web.get("https://www.mi.com/shop/category/list")
# web.maximize_window()

# access tag of magnifier
cats = web.find_elements(By.CSS_SELECTOR, 'div.category-tab > h2')
for i in range(len(cats)):
    cats[i] = re.sub(r'\ue61a', '', cats[i].text)
    print(cats[i])

web.quit()
