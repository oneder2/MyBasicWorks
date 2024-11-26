from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions
from DrissionPage.errors import ElementNotFoundError
import time
import openpyxl

browser_path = "/opt/google/chrome/google-chrome"
main_url = "https://www.mi.com/shop/category/list"

# creat setting object
option = ChromiumOptions()
# set browser path
option.set_browser_path(browser_path)
# create browser page object
page = ChromiumPage(addr_or_opts=option, timeout = 3)
page.get(main_url)

# click the tag
# page.ele("@alt=Xiaomi MIX系列").click()

# input to searching block
page.ele("#search").input("耳机")
# click 
page.ele(".search-btn iconfont").click()

# input data to csv
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "mi shop data"
sheet.append(["name", "price"])

count = 1
# 此时我多么希望存在一个do while
while 1:
    time.sleep(2)
    # roll
    page.run_js('window.scrollBy(0,document.documentElement.scrollHeight)')
    # get good data
    divs = page.eles(".goods-item")
    for div in divs:
        name = div.ele("tag:h2").text
        price = div.ele("x://a/p/span").text
        sheet.append([name, price])
        print(count, name, price)
        count += 1
    try:
        page.ele("x://a[@class='numbers last']").click()
    except ElementNotFoundError as e:
        print("End reached")
        break

wb.save('mi_shop_data.csv')



