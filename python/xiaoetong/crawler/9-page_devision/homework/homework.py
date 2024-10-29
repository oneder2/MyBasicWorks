from bs4 import BeautifulSoup as bs
import requests


headers = {
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }

for chapterIndex in range(5):
    print(chapterIndex)
    url = f'https://www.tangsanbooks.com/book/{50825 + chapterIndex*2}.html'
        
    resHtml = requests.get(url, headers = headers)
    resHtml.encoding = 'utf-8'
    
    rawHtml = resHtml.text
    
    bsHtml = bs(rawHtml, 'lxml')
    
    textList = bsHtml.select('.ui-tabs-panel>p')
    
    with open(f'novel/chapter{chapterIndex + 1}', 'w') as f:
        for text in textList:
            f.write(text.text)
    

#print(beautyHtml[0])



