def heap_sort(elems):
    def siftdown(elems,e,begin,end):
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            # 三个数据，e最小，找到了合适的位置
            if e < elems[j]:
                break
            elems[i] = elems[j]  # elems[j]最小，上移
            i, j = j, j * 2 + 1
        elems[i] = e
    end = len(elems)
    # 建堆
    for i in range(end//2,-1,-1):
        siftdown(elems,elems[i],i,end)
    # 每次取出最小元素放至表的最后,
    for i in range((end-1),0,-1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e,0,i)

def main():
    elems = [3,4,5,2,8,10,4,5,6,2]
    heap_sort(elems)
    print(elems)

if __name__ == '__main__':
    main()
