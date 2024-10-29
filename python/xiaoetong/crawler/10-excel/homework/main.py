import requests
from bs4 import BeautifulSoup as bs
import re
import openpyxl


# judge if specific data exist
def ifEmpty(a):
    try:
        return a[0]
    except IndexError:
        return "Empty"
    return "BADDATA"


headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

# debug usage
pageIndex = 365

# create workbook
animeBook = openpyxl.Workbook()
# delete default sheet
default = animeBook.active
animeBook.remove(default)

# infinite loop
while 1:
    # -> html
    pageUrl = f'https://bgm.tv/anime/browser?sort=rank&page={pageIndex}'
    pageHtml = requests.get(pageUrl, headers = headers)
    # html -> string html
    pageHtml.encoding = 'utf-8'
    stringPageHtml = pageHtml.text
    # string html -> bstree html
    bsPageHtml = bs(stringPageHtml, 'lxml')
    # if this is last page (the page after last page)
    if bsPageHtml.select('.browserFull')[0].get_text() == "":
        break

    # choose working subtitle
    ws = animeBook.create_sheet()
    # modify name of ws1
    ws.title = f'page{pageIndex}'
    # table head
    ws.append(["name", "score", "totalEp", "publishDate", "producers"])

    # preway arrange
    listStringHtml = bsPageHtml.select('.browserFull>li')
    
    # store information
    for eachHtml in listStringHtml:
        # get / list
        name = eachHtml.select('.inner>h3>a')[0].get_text()
        score = eachHtml.select('.inner>.rateInfo>.fade')[0].get_text()

        infoTips = eachHtml.select('.inner>.info.tip')[0].get_text() # mid tool
        totalEp = ifEmpty(re.findall('(\d+话)', infoTips))
        publishDate = ifEmpty(ifEmpty(re.findall('(\d{4}年\d{1,}月\d{1,}日)|(\d{4}年\d{1,}月)|(\d{4}-\d{1,}-\d{1,}){1,})', 
                                                 infoTips)))
        producers = ifEmpty(re.findall('.*\/.*\/\s+(.*)', infoTips))
        
        # add
        ws.append([name, score, totalEp, publishDate, producers])
    
    # debug usage
    if pageIndex == 5 or pageIndex == 370:
        break
    print(f'{pageIndex}')

    # fake recursion
    pageIndex += 1
 
# save xlsx
animeBook.save('famous_anime.xlsx')



