import multiprocessing
import os,time,random
# 多进程版文件夹copy器
def copy_file(queue,file_name,
              source_folder_name,dest_folder_name):
    """ copy文件到指定的路径"""
    f_read = open(source_folder_name + "/" + file_name, "rb")
    f_write = open(dest_folder_name + "/" + file_name, "wb")
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()
    queue.put(file_name)

def main():
    # source_folder_name = input("要复制的文件夹")
    source_folder_name = "E:\PycharmProjects\LearnPy\copy_source_file"
    dest_folder_name = source_folder_name + "[副本]"

    # 创建目标文件夹
    try:
        os.mkdir(dest_folder_name)
    except:
        pass#文件夹已存在，创建失败，什么都不做

    # 获取文件夹中所有文件名
    file_names = os.listdir(source_folder_name)

    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(3)
    for file_name in file_names:
        pool.apply_async(copy_file,args=(queue,file_name,source_folder_name,dest_folder_name))

    pool.close()

    #主进程显示进度
    all_file_num = len(file_names)
    while True:
        file_name = queue.get()
        if file_name in file_names:
            file_names.remove(file_name)

        copy_rate = (all_file_num-len(file_names))*100/all_file_num
        print("\r%.2f...(%s)"%(copy_rate,file_name) + " "*50, end = "")
        if copy_rate>=100:
            break
    print()

if __name__ == '__main__':
    main()