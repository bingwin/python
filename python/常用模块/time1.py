# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
import time

print(time.time())              # 现在时间距离1970年1月1日的秒数
print(int(time.time()))


start = time.time()
for _ in range(100000000):
    pass
end = time.time()
print("循环运行时间:%.2f秒"%(end-start))