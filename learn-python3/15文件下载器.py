from socket import *
import sys

# 服务器参考代码
def get_file_content(file_name):
    """获取文件的内容"""
    try:
        with open(file_name, "rb") as f:
            content = f.read()
        return content
    except:
        print("没有下载的文件%s" % file_name)

def send_file2client(new_client_socket, client_addr):
    recv_data = new_client_socket.recv(1024)
    file_name = recv_data.decode("utf-8")
    print("对方%s请求下载的文件名为:%s" % (str(client_addr),file_name))
    file_content = get_file_content(file_name)
    # 发送数据给客户端
    # 获取打开文件时是以rb方式打开，所以file_content中的数据已经是二进制的格式，因此不需要encode编码
    if file_content:
        new_client_socket.send(file_content)



def main2():
    if len(sys.argv) != 2:
        print("请按照如下方式运行：python3 xxx.py 7890")
        return
    else:
        # 运行方式为python3 xxx.py 7890
        port = int(sys.argv[1])

    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 本地信息
    address = ('', port)
    # 绑定本地信息
    tcp_server_socket.bind(address)
    # 将主动套接字变为被动套接字
    tcp_server_socket.listen(128)
    while True:
        # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        new_client_socket, client_addr = tcp_server_socket.accept()
        send_file2client(new_client_socket,client_addr)
        new_client_socket.close()
    tcp_server_socket.close()


# 客户端参考代码
def main1():

    # 创建socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 目的信息
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))

    # 链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    # 输入需要下载的文件名
    file_name = input("请输入要下载的文件名：")

    # 发送文件下载请求
    tcp_client_socket.send(file_name.encode("utf-8"))
    #接收
    recv_data = tcp_client_socket.recv(1024)
    if recv_data:
        with open("[接收]"+file_name, "wb") as f:
            f.write(recv_data)

    tcp_client_socket.close()

