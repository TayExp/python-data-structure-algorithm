def binary_search1(alist,n,item):
    """二分查找（递归版本）"""

    if n <= 0:
        return False
    mid = n//2
    if alist[mid] == item:
        return True
    elif item < alist[mid]:
        return binary_search1(alist[:mid],mid,item)
    else:
        return binary_search1(alist[mid+1:],n-mid-1,item)
def binary_search2(alist,n,item):
    """二分查找（循环实现）"""
    low = 0
    high = n - 1
    while low <= high:

        mid = (low+high)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            high = mid - 1
        else:
            low = mid+1
    return False

if __name__ == '__main__':

    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 43, 56]
    print(binary_search1(alist,len(alist),10))
    print(binary_search1(alist,len(alist),3.5))
    print(binary_search1(alist,len(alist),100))
    print(binary_search1(alist,len(alist),56))
    print(binary_search2(alist, len(alist), 10))
    print(binary_search2(alist, len(alist), 3.5))
    print(binary_search2(alist, len(alist), 100))
    print(binary_search2(alist, len(alist), 56))
