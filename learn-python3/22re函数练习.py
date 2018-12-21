import re

def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

old = "python = 997"
new = re.sub(r"\d+",add,old)#????????????????
print(new)
new = re.sub(r"\d+",add,new)
print(new)

with open("text.md","rb") as f:
    t1 = f.read()

t = t1.decode("utf-8")
# print(t)
res = re.sub(r"<[^>]*>|&nbsp;|[\r\f\n]{3,}","",t)

print(res)
ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)