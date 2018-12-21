import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息,ip和端口号,必须绑定自己电脑的ip和port
    udp_socket.bind(("", 7866))

    recv_data = udp_socket.recvfrom(1024)# 元组(对方发送数据，对方ip 端口)
    print(recv_data[0].decode())
    udp_socket.close()


if __name__ == '__main__':
    main()
