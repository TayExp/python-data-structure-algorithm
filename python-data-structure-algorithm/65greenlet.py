from greenlet import greenlet
import time
def test1():
    while True:
        print("a")
        gr2.switch()# 手动切换
        time.sleep(0.5)

def test2():
    while True:
        print("b")
        gr1.switch()# 手动切换
        time.sleep(0.5)
gr1 = greenlet(test1)
gr2 = greenlet(test2)
if __name__ == '__main__':
    gr1.switch()# 手动切换