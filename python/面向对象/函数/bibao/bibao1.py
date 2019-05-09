# -*- coding: utf-8 -*-


def print_msg(msg):
# This is the outer enclosing function

    def printer(test):
# This is the nested function
        print(msg)
        print(test)

        return msg                      # 实际return的

    return printer(2)  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
print("11" + another)
# another("312")
# i = another()

# 必须有一个嵌套函数(函数内部的函数)。   print_msg()
# 嵌套函数必须引用封闭函数中定义的值。    printer()
# 闭包函数必须返回嵌套函数              another()



# 也可以不传入函数

def print_msg1():
# This is the outer enclosing function

    def printer1():
# This is the nested function
        print(1)

        # return msg

    return printer1  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg1()
another()

