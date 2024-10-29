import requests
from bs4 import BeautifulSoup as bs
import re


indexUrl = 'https://www.tangsanbooks.com/xs/wanxiangzhiwang'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }

resHtml = requests.get(indexUrl, headers = headers)
resHtmlText = resHtml.text

bsHtml = bs(resHtmlText, 'lxml')

chapterHtmlList = bsHtml.select('.list-chapter>li>a')

count = 1
toIndex = 10
for chapterHtml in chapterHtmlList:
    chapterUrl = chapterHtml['href']

    resHtml = requests.get(chapterUrl, headers = headers)
    resHtml.encoding = 'utf-8'

    rawHtml = resHtml.text.replace('  ', '\n\n')
    bsHtml = bs(rawHtml, 'lxml')

    textList = bsHtml.select('.ui-tabs-panel>p')

    with open(f'novel/{chapterHtml.text}', 'w') as f:
        for text in textList:
            f.write(text.text)

    print(count)
    count+=1
    if count == toIndex + 1:
        break
    break


