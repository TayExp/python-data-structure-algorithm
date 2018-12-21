import socket
import re

def service_client(new_socket):
    """为这个客户端返回数据"""
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode("utf-8")
    print(">"*20)
    request_lines = request.splitlines()
    print(request_lines)
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        file_name = "./html"+file_name

    print(file_name)
    try:
        f = open(file_name,"rb")
        # 返回http格式点的数据给浏览器

    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response_body = "not found by me".encode("utf-8")
    else:
        response = "HTTP/1.1 200 OK\r\n"  # Windows，\r\n表示换行
        response += "\r\n"
        response_body = f.read()
        f.close()
    new_socket.send(response.encode("utf-8"))
    new_socket.send(response_body)
    new_socket.close()

def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，下次运行程序时可立即绑定7890端口
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_server.bind(("", 7890))
    #变为监听套接字
    tcp_server.listen(128)
    #等待客户端的连接
    while True:
        new_socket,client_addr = tcp_server.accept()
    # 为这个客户端服务
        service_client(new_socket)
    tcp_server.close()
if __name__ == '__main__':
    main()