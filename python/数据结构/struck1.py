# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# struct的pack函数把任意数据类型变成字符串：

# bytes是Python 3中特有的，Python 2 里不区分bytes和str。
# 准确地讲，Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节，所以，字节数组＝str

import struct

print(struct.pack('>I', 10240099))



print(struct.pack('!HIH', 1, 2, 3))


# 根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数。
print(struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80'))
print(struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x83\x81'))

