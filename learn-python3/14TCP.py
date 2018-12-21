import socket

#客户端，另一端是服务器
def main1():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #链接服务器
    server_ip = input("ip:")
    server_port = input("port:")
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    send_data = input("data:")
    tcp_socket.send(send_data.encode("utf-8"))

    #接收数据
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))

    tcp_socket.close()

#服务器
def main2():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_socket.bind("", 7788)
    # 被动
    tcp_socket.listen(128)
    while True:
        print("等待一个新的客户端的链接")
        # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        new_client_socket, client_addr = tcp_socket.accept()
        # 被连接了，接下来是服务
        print(client_addr)
        while True:
            # 接收，只接收数据，无需地址recv
            recv_data = new_client_socket.recv(1024)
            if recv_data: #接收数据解堵塞
                print(recv_data.decode("utf-8"))
                # 回送
                new_client_socket.send("ok".encode("utf-8"))
            else:#为空,返回的长度为0,（客户端关闭了）解堵塞
                break
    new_client_socket.close()

    tcp_socket.close()

