import requests

kv = {"user-agent":"Mozilla/5.0"}
url = "https://www.amazon.cn/dp/B07GVXHCXH/ref=cngwdyfloorv2_recs_0/458-7995391-0211127?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=CSNBFGEN53ND82PB0SV4&pf_rd_r=CSNBFGEN53ND82PB0SV4&pf_rd_t=36701&pf_rd_p=db4e96ef-5fc1-47f8-92b2-b9a5e737b326&pf_rd_p=db4e96ef-5fc1-47f8-92b2-b9a5e737b326&pf_rd_i=desktop"
try:
    r = requests.get(url, headers = kv)
    # r.raise_for_status()
    print(r.status_code)
    r.encoding = r.apparent_encoding

    print(r.text[:1000])
    print(r.request.headers

except:
    print("爬取失败")