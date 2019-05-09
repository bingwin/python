# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 字符串或串(String)是由数字、字母、下划线组成的一串字符。

s = 'abcdef'
print(s[1:5])  # 输出bcde

# \n 是换行符
print ("eqw\ndas")

# 撇号位于两个引号之间，因此python解释器能够正确地理解这个字符串
message = "one ' das "
print(message)

# 加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：

str1 = 'Hello World!'

print str1  # 输出完整字符串
print str1[0]  # 输出字符串中的第一个字符
print str1[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str1[2:]  # 输出从第三个字符开始的字符串
print str1 * 2  # 输出字符串两次
print str1 + "TEST"  # 输出连接的字符串

# 将对象 x 转换为字符串

a = 1
b = "dasfa" + str(a)
print(b)

print(len(b))  # 计算字符串个数

print("---------------------------------")

# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 我们还可以使用s[a:b:c]的形式对s在a和b之间以c间隔进行取值
s = "bicycle"
print(s[::3])   # bye
print(s[::-1])  # elcycib
print(s[::-2])  # eccb

# +	字符串连接
# >>>a + b
# 'HelloPython'
# *	重复输出字符串
# >>>a * 2
# 'HelloHello'
# []	通过索引获取字符串中字符
# >>>a[1]
# 'e'
# [ : ]	截取字符串中的一部分
# >>>a[1:4]
# 'ell'
# in	成员运算符 - 如果字符串中包含给定的字符返回 True
# >>>"H" in a
# True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
# >>>"M" not in a
# True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# >>>print r'\n'
# \n
# >>> print R'\n'
# \n


a = "dsad"
print(bool(a))
