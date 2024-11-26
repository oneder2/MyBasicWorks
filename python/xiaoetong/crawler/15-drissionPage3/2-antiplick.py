from DrissionPage._pages.chrimium_page import ChromiumPage;


page = ChromiuPage();
page.get('https://cszg.mca.gov.cn/biz/ma/csmh/filter/slideCapchaindex.html');


# to tell if CAPTCHA exist
# flicking grpah
captchaImg = page.ele('#captchaImg');
threshod = 20
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

