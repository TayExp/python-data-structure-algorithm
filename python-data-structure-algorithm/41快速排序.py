def quick_sort(alist,low, high):
    """快速排序"""
    if low >= high:
        return
    mid_value = alist[low]#以这个数为分界
    i = low
    j = high
    while i<j:
        while i < j and alist[j] >= mid_value:
            j -= 1
        alist[i] = alist[j]#这个j这个位置没用了
        while i < j and alist[i] <= mid_value:
            i += 1
        alist[j] = alist[i]#这个i这个位置没用了
    quick_sort(alist,low,i-1)
    quick_sort(alist,i+1,high)

if __name__ == '__main__':
    alist=[56,43,23,4,3,2,10,9,8,7,6,5,1,3]
    quick_sort(alist,0,len(alist)-1)
    print(alist)