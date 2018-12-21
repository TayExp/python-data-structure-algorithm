import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息,ip和端口号,必须绑定自己电脑的ip和port
    # udp_socket.bind(("", 7866))
    while True:
        # des_add = ("192.168.1.138", 8080)
        # des_add = ("10.138.250.10", 8080)
        des_add = ("10.138.188.21", 8080)
        send_data = input("输入发送数据")
        if send_data == "break":
            break
        udp_socket.sendto(send_data.encode("utf-8"), des_add)

    # recv_data = udp_socket.recvfrom(1024)# 元组(对方发送数据，对方ip 端口)
    # print(recv_data[0])
    udp_socket.close()


if __name__ == '__main__':
    main()
