
def shell_sort(alist,n):
    """希尔排序"""
    # n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap,n):
            # j = gap,gap+1,...n-1
            i = j
            while i>gap-1:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap = gap // 2


if __name__ == '__main__':
    alist=[56,43,23,4,3,2,10,9,8,7,6,5,1,3]
    shell_sort(alist,len(alist))
    print(alist)