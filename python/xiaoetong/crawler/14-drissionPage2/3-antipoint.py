from DrissionPage._pages.chromium_page import ChromiumPage
import time


# access page
page = ChromiumPage()
page.get('https://www.chaojiying.com/user/login')

# access page changer
next_tag = page.ele('@data-page=next')
# click
next_tag.click()

# load tags
time.sleep(2)
div = page.ele('.mask').attr('style')
# if div is None, no check, no operation needed
# if div is not None:
if div is not None:
    box = page.ele('.verifybox-bottom')
    box.get_screenshot('box.png')
    # to be continue

    
