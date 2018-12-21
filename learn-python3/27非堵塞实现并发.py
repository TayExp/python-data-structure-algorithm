import socket
import re
import time
def service_client(new_socket,recv_data):
    """为这个客户端返回数据"""
    # GET / HTTP/1.1
    request = recv_data
    print(">" * 20)
    request_lines = request.splitlines()
    print(request_lines)
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        file_name = "./html" + file_name

    print(file_name)
    try:
        f = open(file_name, "rb")
        # 返回http格式点的数据给浏览器

    except:
        response_body = "not found by me"
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header += "Content-Length:%d\r\n" %len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body.encode("utf-8")

    else:
        response_body = f.read()
        f.close()
        response_header = "HTTP/1.1 200 OK\r\n"  # Windows，\r\n表示换行
        response_header += "Content-Length:%d\r\n" %len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

    new_socket.send(response)


def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，下次运行程序时可立即绑定7890端口
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(("", 7890))
    # 变为监听套接字
    tcp_server.listen(128)
    tcp_server.setblocking(False)
    # 等待客户端的连接
    client_socket_list = []
    while True:
        time.sleep(1)

        try:
            new_socket, client_addr = tcp_server.accept()
        except Exception as ret1:
            print("%s--没有客户端到来--"%ret1)
        else:
            print("--到了一个新的客户端")
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as ret:
                print("%s--这个客户端没有发送数据--"%ret)
            else:
                if recv_data:
                    print("发来数据")
                    service_client(client_socket, recv_data.decode("utf-8"))
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print("关闭了一个客户端")
        print(client_socket_list)
    tcp_server.close()


if __name__ == '__main__':
    main()