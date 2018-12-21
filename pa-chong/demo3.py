import requests


kv = {"wd": "Python"}
#try:
r = requests.get("http://www.baidu.com/s", params = kv)
    # r.raise_for_status()
print(r.status_code)
    #r.encoding = r.apparent_encoding
print(r.request.url)
   # print(r.text[:1000])
    #print(r.request.headers
print(len(r.text))
#except:
   # print("爬取失败")