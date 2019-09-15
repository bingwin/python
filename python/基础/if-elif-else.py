# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

#if-elif-else
#4岁免费 4-18岁5元 18岁以上10元


def if_el(age):
    if age < 30:
        print(0)
    elif age > 20:
        print(5)
    elif age == 25:
        print(10)
if_el(25)

# else:
#     print(10)


# for i in range(5):
#     print(i)


var = None
def fun_not_var(var_data):
    if not var_data:
        print('哈哈哈哈')
    else:
        print('嘿嘿嘿')
fun_not_var(var)
# 在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
