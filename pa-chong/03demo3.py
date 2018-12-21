# 股票数据定向爬虫
import requests
import re
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url, code='utf-8'):
    #try:
    r = requests.get(url, timeout=30)
        #r.raise_for_status()
    r.encoding = code
    return r.text
    #except:
     #   return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all("a")
    for i in a:
        try:
            href = i.attrs["href"]
            stock_num = re.findall(r"[s][hz]\d{6}", href)
            if stock_num:
                lst.append(stock_num[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        print(url)
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, "html.parser")
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            #print(type(stockInfo))
            #print(stockInfo)
            stock_name = stockInfo.find_all(attrs={'class': "bets-name"})[0]
            print(stock_name)
            infoDict.update({'股票名称': stock_name.text})
            keyList = stockInfo.find_all('dt') #按顺序？？
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(str(infoDict) + "\n"))
                count = count + 1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst), end=''))
        except:

             count = count + 1
             print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst), end=''))
             traceback.print_exc()
             continue


def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = 'E://BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    # print(slist)
    getStockInfo(slist, stock_info_url, output_file)


if __name__ == '__main__':
    main()