from lxml import etree


# to avoid requests reqeat, we can save the string of lianjia.html first, and load it there
fileContent = ""
with open("lianjia.html", "r", encoding = "utf-8") as f:
    fileContent = f.read()
myTree = etree.HTML(fileContent)

# analyze data
# title label, obtain form xpath expression
# tree.xpath('xpath expression')
# return a list, the label object obtained by expression

# 1. the very left slash "/" root label: absolute address finding
# print(myTree.xpath('/html/head/title'))

# 2. // find label from any previous address:
# get all label
# print(myTree.xpath('//div'))

# 3. get content from label
# print(myTree.xpath('//span/text()'))

# element limitation
# print(myTree.xpath('//h2/span/text()'))

#myUrl = 'https://cs.lianjia.com/ershoufang/104113837527.html'

# multi labels
# label_name[@element_name="enelemt_value"]
#print(myTree.xpath('//a[@href="https://cs.lianjia.com/ershoufang/104113687104.html"]/text()'))

print(myTree.xpath('//div[@class="info clear"]//a/@href'))

"""
start:
    / absolute path
    // from anypath
not start:
    / a single path
    // from current path, search anypath with following label

get text content: 
    /text() content under the last label
    //text() content from each off spring of the last label (store in list)

element limit:
    label[@element_name=element_value]

get element:
    label/@element_name

"""




