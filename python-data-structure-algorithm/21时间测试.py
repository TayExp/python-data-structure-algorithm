import time

start_time = time.time()
#返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
time.localtime()
time.asctime()

# Python内置类型：timeit模块
import timeit
# 测试一小段代码的执行速度
#stmt 是要测试的代码语句,如函数名()
#setup是 运行代码时需要的设置
#timer是一个定时器函数，与平台有关
#python列表类型不同操作的时间效率