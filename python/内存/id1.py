# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Python中的可变对象和不可变对象
# https://www.cnblogs.com/sun-haiyu/p/7096918.html

# 不可变对象，该对象所指向的内存中的值不能被改变。当改变某个变量时候，由于其所指的值不能被改变，相当于把原来的值复制一份后再改变，这会开辟一个新的地址，变量再指向这个新的地址。

# 可变对象，该对象所指向的内存中的值可以被改变。变量（准确的说是引用）改变后，实际上是其所指的值直接发生改变，并没有发生复制行为，也没有开辟新的出地址，通俗点说就是原地改变。

# Python中，数值类型（int和float）、字符串str、元组tuple都是不可变类型。

# 而列表list、字典dict、集合set是可变类型。

# **容器序列**
# 	list，tuple，deque
# **扁平序列**
# 	str，bytes，bytearray，array.arry
# **可变序列**
# 	list，deque，bytearray，array
# **不可变序列**
# 	str ，tupple，bytes

# 序列是python 非常重要一种协议， 如何把一个类变成一个序列类，这个序列类的重要性. 请看下边的截图，就是所有的序列类型的列表. 可以按照两个维度进行区分.
# 1.按照存储数据类型区别 可以分为 容器序列和扁平序列.
# 容器序列是可以放置任何数据类型，放什么东西都可以是个容器
# 扁平序列是可以用for 循环遍历，其中array 必须指明数据类型.
# 2.按照可变性，可以分为 可变序列和不可变序列
# 可变意思是 创建之后可以添加数据的.
# 不可变意思创建后就不能修改.

# list、set和dictionary 都是可改变的，比如可以通过list.append()，set.remove()，dict['key'] = value对其进行修改，所以它们都是不可哈希的；
#
# 而tuple和string是不可变的，只可以做复制或者切片等操作，所以它们就是可哈希的


a = 2
b = 2
c = a + 0
c += 0

print(id(a), id(b), id(2))  # id都相同   2在内存中的地址是固定的
print(c is b)  # True

print('————————————————————————————————————————————————————————————————')

astr = 'good'
bstr = 'good'
cstr = astr + ''
print(cstr is bstr)  # True
print(id(astr), id(bstr), id('good'))  # 三个id相同    指向good的地址相同

astr = 'good'
print(id(astr))
astr += 'aa'
print(id(astr))  # id和上面的不一样

# 对于str、int、float只要在它们在类型相同的情况下，值也相同，那么它们的id相同。
# 由于是不可变对象，变量对应内存的值不允许被改变。当变量要改变时，实际上是把原来的值复制一份后再改变，开辟一个新的地址，astr再指向这个新的地址（所以前后astr的id不一样），
# 原来astr对应的值因为不再有对象指向它,就会被垃圾回收。这对于int和float类型也是一样的

print('————————————————————————————————————————————————————————————————')

# 相同的数值，tuple的id也不同 但是不可变类型
add = (1, 2, 3)
aee = (1, 2, 3)
print(id(add), id(aee), id((1, 2, 3)))  # id各不相同

aee = (1, 2, 3)
print(id(aee))
aee += ()  # 加空元组
print(id(aee))  # id变了！
print(aee)   # （1 ，2，3）

add = (1, 2, 3)
aee = add
print(id(aee), id(add))  # 这两个id一样
aee += (4, 5, 6)
print(id(aee))  # aee的id变了！
print(id(add))  # add的没有变
print(add)  # add还是(1, 2, 3)没有变

print('————————————————————————————————————————————————————————————————')

# 相同的数值，list的id也不同 但是是可变类型
lis = [1, 2, 3]
lis2 = [1, 2, 3]
# 虽然它们的内容一样，但是它们指向的是不同的内存地址
print(lis is lis2)
print(id(lis), id(lis2), id([1, 2, 3]))  # 三个id都不同

alist = [1, 2, 3]
# alist实际上是对对象的引用，blist = alist即引用的传递，现在两个引用都指向了同一个对象（地址）
blist = alist
print(id(alist), id(blist))  # id一样
# 所以其中一个变化，会影响到另外一个
blist.append(4)
print(alist)  # 改变blist, alist也变成了[1 ,2 ,3 4]
print(id(alist), id(blist))  # id一样，和上面值没有改变时候的id也一样

print('————————————————————————————————————————————————————————————————')

# 再看看set
# 相同的数值，set的id也不同 但是是可变类型
abb = {1, 2, 3}
acc = abb
print(id(abb), id(acc))
acc.add(4)
print(abb)  # {1, 2, 3, 4}
print(id(abb), id(acc))  # 相等