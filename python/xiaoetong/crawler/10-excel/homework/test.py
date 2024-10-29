from bs4 import BeautifulSoup

# 示例 HTML 文档
html_doc = """
<html>
<head><title>示例页面</title></head>
<body>
    <h1 class="header">欢迎来到我的网站</h1>
    <p class="content">这是一个段落。</p>
    <p class="content highlight">这是另一个段落，带有高亮。</p>
    <a href="https://example.com" class="link">链接</a>
</body>
</html>
"""

# 创建 BeautifulSoup 对象，使用 lxml 解析器
soup = BeautifulSoup(html_doc, 'lxml')

# 使用 select 方法选择所有 <p> 标签
paragraphs = soup.select('p')

# 读取并打印每个 <p> 标签的文本内容
for p in paragraphs:
    print(p.get_text())

