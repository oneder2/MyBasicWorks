from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# create service object, arrange path of the driver
service = Service("/home/gellar/opt/chromedriver-linux64/chromedriver")
# create web object
web = webdriver.Chrome(service = service)
# open page baidu, no need to specify "get" or "post"
web.get("https://www.dangdang.com/")
web.maximize_window()

#name = input("请输入你想要查询的商品：")
name ="python"
# access tag of searching block
input_tag = web.find_element(By.ID, 'key_S')
input_tag.send_keys(name)
# access tag of magnifier
but_tag = web.find_element(By.CLASS_NAME, 'button')
# realize clicking: tagobject.click()
but_tag.click()

# get data
# there is no same elemnt with every tag
# so we need parent element
lis = web.find_elements(By.XPATH, '//ul[@class="bigimg"]/li')

COUNT = 1
for li in lis:
    # li = lis[i]
    # via tag object, get .txt
    # book_name = li.find_element(By.NAME, 'itemlist-title').text
    book_name = li.find_element(By.NAME, 'itemlist-title').get_attribute('title')
    price = li.find_element(By.CLASS_NAME, 'search_now_price').text
    
    try:
        author = li.find_element(By.NAME, 'itemlist-author').get_attribute('title')
    except:
        author = "none"
    
    try:
        date =  li.find_element(By.XPATH, '//p[@class="search_book_author"]/span[2]').text
    except:
        date = "none"
    
    try:
        cbs = li.find_element(By.NAME, 'P_cbs').text
    except:
        cbs = "none"
    
    try:
        command_num = li.find_element(By.CLASS_NAME, 'search_comment_num').text
    except:
        command_num = "0"

    print(COUNT, book_name, price, author, date, cbs, command_num)
    COUNT += 1

web.quit()


# via xpat
#//input[@id="kw"]
# tag = web.find_element(By.XPATH, '//input[@id="kw"]')
# tag.send_keys('python')




