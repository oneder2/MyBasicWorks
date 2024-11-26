from DrissionPage._pages.chromium_page import ChromiumPage
from chaojiying import Char


# create page object
page = ChromiumPage()
page.get('https://www.chaojiying.com/user/login')

# 1. access username, password
username_tag = page.ele('@name=user')
password_tag = page.ele('@name=pass')

# 2. input username, password
username_tag.input('@name=user')
password_tag.input('@name=pass')

# 3. access CAPTCHA graph
img_binary = page.ele('x://form//img').src()
chaojiying = Chaojiying_Client('root', 'root', '932618') # 假装我有一个账户
# dictionary = PostPic(picture_bytedata, recognization_type)
res = chaojiying.PostPic(imi, 1902)

# 4. convey to super ego
s = res['pic_str'] # get recognize result

# 5. recognize the CAPTCHA
captcha_tag = page.ele('@name=imgtxt')

# 6. input CAPTCHA
yzm_tag.input(s)

# 7. click login button
login_tag = page.ele('.login_form_input_submit')
login_tag.click()


