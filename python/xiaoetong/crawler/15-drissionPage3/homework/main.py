from DrissionPage._pages.chromium_page import ChromiumPage;


page = ChromiumPage();
page.get('https://study.xiaoe-tech.com/t_l/learnLogin#/acount');

# change to password login
page.ele('.account-title-item password-item').click()

# enter phone number and password
password = input('please enter password: ')
if page.ele('.ss-input__inner').text == "":
    page.ele('.ss-input__inner').input(phone_num)

page.ele('@data-sensors=登录_登录页_点击设置密码').input(password)

# agree the conceptions
try:
    page.ele('.ss-checkbox__input').click()
except Exception as e:
    pass

# press login, get secure code
page.ele('.login-btn big-button').click()

exit(0)
# 以上是我力所能及的范围
# 由于我使用超级鹰并不安全，所以以下是我臆想的解法，并没有实际解答

# flicker check page appear
# to tell if CAPTCHA exist
# flicking grpah
captchaImg = page.ele('#captchaImg');
# 目测小鹅通的滑块很灵
threshod = 0
if captchImg is not None:
    # 1. get ragged graph
    img_data = page.ele('#oriImg').src();
    chaojiying = Chaojiying_Client('root', 'root', '932618');
    chaojiying.PostPic(img_data, 9101);
    xy = res['pic_str'];
    x = int(xy.split(',')[0]) - threshod;

    # get slider tag
    slider = page.ele('#slider');
    # press, and hold the slider tag
    page.actions.hold(slider);
    page.actions.move(offset_x = x);
    # stop holding
    page.actions.release(slider);

time.sleep(2)
# get/reach/gather/mine/collect data
trs = page.eles('x://table//tr');
# if trs lenght == 0
if len(trs) == 0:
    for tr in trs[1:]:
        tr.eles('tag:td')
        for td in tds:
            print(td.text)

