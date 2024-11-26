from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions


browser_path = "/opt/google/chrome/google-chrome"
main_url = "https://www.mi.com/shop/category/list"

# creat setting object
option = ChromiumOptions()
# set browser path
option.set_browser_path(browser_path)
# create browser page object
page = ChromiumPage(addr_or_opts=option)
page.get(main_url)

#print(page.html)

#"""
# By expression: "tag:xxx"
# if expression exist, retrun tag object, othervise return none
print(page.ele('tag:title'))
# if expression exist, retrun a list contains tagged object, othervise retrun empty list
print(page.eles('tag:title'))

# By id: "#xxx"
print(page.ele('#app'))

# By class: ".xxx"
print(page.ele('.breadcrumbs'))

# By name: "@name=xxx"
print(page.ele('@name=description'))

# By xpath "xpath:(xpath expression)"
print(page.ele('xpath://div[@id="app"]'))
print(page.ele('x://div[@id="app"]'))
#"""

print(page.ele("@name=description").attr("content"))








