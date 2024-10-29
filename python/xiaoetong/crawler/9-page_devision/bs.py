from bs4 import BeautifulSoup

with open('lianjia.html', 'r', encoding = 'utf-8') as f:
    htmlCode = f.read()

bs = BeautifulSoup(htmlCode, 'lxml')

#print(bs.title)
#print(bs.div)

info = bs.findAll('div', class_='positionInfo')

for i in info:
    print(i.text)
    print(i.string)
    break


