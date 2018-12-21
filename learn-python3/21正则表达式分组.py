import re
# 匹配分组的练习
result = re.match(r"([^-]*)-(\d+)","010-12345678")
print(result.group(0))
print(result.group(1))
print(result.group(2))
# 匹配出<html>hh</html>

ret1 = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</hmml>,<html>hh</html>")
if ret1:
    print(ret1.group())
print("-"*20)
ret2 = re.match(r"<([a-zA-Z]*)>\w*</\1*>", "<html>hh</htl>")
if ret2:
    print(ret2.group())
print("-"*20)
ret3 = re.match(r"<([a-zA-Z]*)>\w*</\1*>", "<html>hh</html>")
if ret3:
    print(ret3.group())
print("-"*20,"\n","-"*20)

# 匹配出<html><h1>www.itcast.cn</h1></html>
labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

for label in labels:
    ret = re.match(r"<(?P<N1>\w*)><(?P<N2>\w*)>.*</(?P=N2)></(?P=N1)>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)