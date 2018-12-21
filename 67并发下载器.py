from gevent import monkey
import time
import gevent
import urllib.request

monkey.patch_all()

def my_download(file_name,url):
    print("get: %s" %url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    with open(file_name, "wb") as f:
        f.write(data)
    print("%d bytes received from %s"%(len(data),url))

gevent.joinall([gevent.spawn(my_download,"file2.html","http://www.itcast.cn/"),
                gevent.spawn(my_download,"file3.html","http://www.itheima.com/"),
                gevent.spawn(my_download, "file1.html", "http://www.baidu.com/")])
