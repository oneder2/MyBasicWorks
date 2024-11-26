from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions


browser_path = "/opt/google/chrome/google-chrome"
main_url = "https://www.mi.com/shop/category/list"

# creat setting object
option = ChromiumOptions()
# set browser path
option.set_browser_path(browser_path)
# create browser page object
page = ChromiumPage(addr_or_opts=option, timeout=.1)
page.get(main_url)

# Set timeout limitation
page.set.timeouts(3)
print(page.ele("tag:title").attr("content"))
