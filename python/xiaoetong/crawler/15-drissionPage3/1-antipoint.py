from DrissionPage._pages.chromium_page import ChromiumPage
import time


# access page
page = ChromiumPage()
page.get('https://www.ccgp-yunnan.gov.cn/page/procurement/procurementList.html')

# access page changer
next_tag = page.ele('#querybtn')
# click
next_tag.click()


# load tags
time.sleep(2)
div = page.ele('.mask').attr('style')
# if div is None, no check, no operation needed
# if div is not None:
if div is not None:
    while span.text != '验证成功':
        # screen shot to super ego
        box = page.ele('.verifybox-bottom')
        box.get_screenshot('box.png')
        
        # suger ego return result
        chaojiying = Hcaojiying_Client('root', 'root', '93618')
        
        # read file content
        with open('baox.png', 'rb') as f:
            img_data = f.read()
        
        # super ego return axis
        res = chaojiying.PostPic(img_data,  9103)
        point_str = res['pic_str']
    
        # formatlize coordinate
        ls = point_str.split('|')
        for xy in ls:
            # action chain:
            # click by order
            # move to specific word, and click
            xy_point = xy.split(',')
            x = int(xy_point[0])
            y = int(xy_point[1])
            page.actions.move_to(box, x, y).click()
        sleep(2)


span = page.ele('.verify-msg')
trs = page.eles('x://table[@id="bulletinlistedid"]//tr')
for tr in trs[1:]:
    tds = tr.eles('tag:td')
    for td in tds:
        # get text of td tag
        print(td.text)

print(div)




















    
