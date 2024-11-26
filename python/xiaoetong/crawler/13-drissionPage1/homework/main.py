from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions
from DrissionPage.errors import ElementNotFoundError
import time
import openpyxl

browser_path = "/opt/google/chrome/google-chrome"
main_url = "https://www.dangdang.com/"

# creat setting object
option = ChromiumOptions()
# set browser path
option.set_browser_path(browser_path)
# create browser page object
page = ChromiumPage(addr_or_opts=option, timeout = 10)
page.get(main_url)

# click the tag
# page.ele("@alt=Xiaomi MIX系列").click()

# input to searching block
search_input = input("Please input wait you want to seach: ")
page.ele(".label_search").input(search_input)
# click 
page.ele(".button").click()

# input data to xlsx
wb = openpyxl.Workbook()
sheet = wb.active
wb.remove(wb["Sheet"])

count = 1
# 此时我多么希望存在一个do while
for index in range(1, 6):
    # initialize subsheet
    sheet = wb.create_sheet(title=f"{search_input}_page_{index}")
    sheet.append(["name", "price"])

    time.sleep(3)
    # roll
#    page.run_js('window.scrollBy(0,document.documentElement.scrollHeight)')
    # get good data
    lis = page.ele(".bigimg").eles("tag:li")
    for li in lis:
        name = li.ele("x://p[@class='name']/a").text
        price = li.ele("x://p[@class='price']/span[@class='search_now_price']").text
        sheet.append([name, price])
        print(count, name, price)
        count += 1

    try:
        page.ele(".next").ele("x://a").click()
    except ElementNotFoundError as e:
        print("End reached")
        break
    

wb.save(f'{search_input}_search_result.xlsx')



