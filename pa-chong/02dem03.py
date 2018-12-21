# 定向爬虫
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
        soup = BeautifulSoup(html, "html.parser")
        for tr in soup.find('tbody').children:
            # 排除字符串节点
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    tp = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tp.format("排名", "学校", "评分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tp.format(u[0], u[1], u[2], chr(12288)))

def main():
    uinfo = []
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

if __name__ == '__main__':
    main()