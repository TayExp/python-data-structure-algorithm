import requests
import re
# import bs4
# from bs4 import BeautifulSoup

# url2 = "https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44"
def getHTMLText(url):
    # try:
        r = requests.get(url, timeout=30)
    #    r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    # except:
    #    return ""

def parsePage(ilt, html):
    #try：
    plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
    for i in range(len(plt)):
        price = eval(plt[i].split(':')[1])
        title = eval(tlt[i].split(':')[1])
        ilt.append([price, title])

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 3;
    # 起始页
    start_url = "https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
    infoList = []
    for i in range(depth):
        url = start_url + "&s=" +str(44*i)
        html = getHTMLText(url)
        parsePage(infoList, html)
        printGoodsList(infoList)

if __name__ == '__main__':
    main()