from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# 查找a标签
# find_all(name/True，attrs, recursive=True/False,string="")
for link in soup.find_all(['a', 'b']):
    print(link.get("href"))
for tag in soup.find_all(True):
    print(tag.name)

import re
# b开头的标签
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

print(soup.find_all('p', 'course'))

# 标注属性检索
print(soup.find_all(id='link1'))

# 检测字符串
print(soup.find_all(string="Basic Python"))

print(soup.find_all(string=re.compile("python")))

# ()代表.find_all()