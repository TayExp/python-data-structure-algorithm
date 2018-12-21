# 爬取并保存图片
import requests
import os


url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1540500695270&di=d3b3135ba9a11c928d3c853d8ee8be3d&imgtype=0&src=http%3A%2F%2Fimg1.gamersky.com%2Fimage2015%2F12%2F20151203wyc_2%2Fgamersky_01small_02_201512310335E.jpg"
root = "E:/pics/"
# path = root + url.split('/')[-1]
path = root + "gb.jpg"
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        # print(r.status_code)
        #保存图片
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("爬取失败")