# -*- coding: utf-8 -*-



#第一版
def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        # print(t)
        # return func()       # 带括号执行 print "hello!"
        return func       # 不带括号 不执行print "hello!"
    return wrapper()        # 带括号执行 print "hello!"
    # return wrapper          # 不带括号不执行 print "hello!"

# say_hello = debug(say_hello)  # 添加功能并保持原函数名不变

@debug
def say_hello():
    print "hello!"




#第二版
def debug_2(code):
    def wrapper(func):
        print "[DEBUG]: enter {}()".format(func.__name__)
        print(code)
        # print(t)
        # return func()
        return func
    return wrapper

# say_hello = debug(say_hello)  # 添加功能并保持原函数名不变

@debug_2(code=100)
def say_hello_2():
    print "hello_2!"




def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging('INFO')
def say(something):
    print "say {}!".format(something)

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

if __name__ == '__main__':
    say_hello()
    say_hello_2()
    say('hello')
    do("my work")