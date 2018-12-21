import requests


url = "https://item.jd.com/6961588.html?jd_pop=b71dc1f0-850e-416d-b213-3b395ee8bb06"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")