
def insert_sort(alist,n):
    for i in range(1,n):
        # 将i插入合适位置
        j = i
        while j > 0 :
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
                j = j - 1
            else:
                break

if __name__ == '__main__':
    alist=[56,43,23,4,3,2,10,9,8,7,6,5,1,3]
    insert_sort(alist,len(alist))
    print(alist)

