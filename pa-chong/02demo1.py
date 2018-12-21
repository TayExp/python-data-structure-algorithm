import requests
from bs4 import BeautifulSoup


r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

# beautifulsoup库是解析、遍历、维护“标签树”的功能库

# 第一个参数是html格式的信息"<p>data</p>"，
# 第二个参数是解析器类型:
# soup = BeautifulSoup(open("D://S.html"), "html.parser")
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
print(soup.title)

# a标签的名字
print(soup.a.name)

# a标签父标签的名字
print(soup.a.parent.name)

# 属性
print(soup.a.attrs)

#
print(soup.a.attrs['class'])
print(soup.a.attrs['href'])
print(soup.a.string)

# navigableString可以跨越多个标签层次
print(soup.p.string)
print(type(soup.p.String))

