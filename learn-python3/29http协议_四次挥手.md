* HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信
* 安装好Chrome浏览器后，打开Chrome，在菜单中选择“视图”，“开发者”，“开发者工具”，就可以显示开发者工具
    1. Elements显示网页的结构
    2. Network显示浏览器和服务器的通信
    3. 浏览器请求：
    
            GET / HTTP/1.1 #url，以/开头
            # get（请求资源）,post(附带用户数据)
            # 1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度
            HOST: www.sina.com # 请求的域名
    4. 服务器响应：
    
            # HEADER
            HTTP/1.1 200 OK
            # 200成功，3xx重定向， 4xx客户端发送错误，5xx服务器处理错误
            Content-type: text/html# 浏览器以此判断相应内容类型
            #BODY
    5. 浏览器解析html，显示页面，
    并根据链接再发送http请求给服务器拿到图片、js、csss等
  
  
### tcp三次握手和四次挥手
* 三次握手建立连接
    1. C->S：syn 11
    2. S->C：ack12 + syn44
    3. C->S: ack45
   
* 四次挥手断开连接
    1. C.close()关闭发送->S： 
    2. S关闭接收，我收到了->C
    3. S.close()关闭发送->C
    4. C关闭接收，我收到了，并等待两个MSL释放自己->S
    5. 万一S没收到的话就再发
    
  