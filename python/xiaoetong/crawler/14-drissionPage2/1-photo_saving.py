from DrissionPage._pages.chromium_page import ChromiumPage
import os


page = ChromiumPage()
# open website
page.get('https://101.qq.com/#/hero')

lis = page.eles('.list-item')

# create file folder
img_path = 'photo'
if not os.path.exists(img_path):
    os.mkdir(img_path)

for li in lis:
    hero_name = li.ele('.hero-name').text
    # print(li.ele('tag:img').src())
    img = li.ele('tag:img')
    # path: saving path
    img.save(path=img_path, name=f'{hero_name}.png')

