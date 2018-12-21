def merge_sort(alist,n):
    """归并排序"""
    if n <= 1:
        return alist
    mid = n//2
    left = merge_sort(alist[:mid],mid)
    right = merge_sort(alist[mid:],n-mid)
    #合并两个列表
    lp = 0
    rp = 0
    result = []
    while lp < len(left) and rp < len(right):
        if left[lp] <= right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    if lp == len(left):
        result += right[rp:]
    else:
        result += left[lp:]
    return result
if __name__ == '__main__':
    alist=[56,43,23,4,3,2,10,9,8,7,6,5,1,3]
    print(merge_sort(alist,len(alist)-1))
    print(alist)