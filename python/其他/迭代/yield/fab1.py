# encoding:UTF-8
import sys


# Num02–>生成器
#
# 作用：
#
# >延迟操作。也就是在需要的时候才产生结果，不是立即产生结果。
#
# 注意事项：
#
# >生成器是只能遍历一次的。
# >生成器是一类特殊的迭代器。

def fab_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
        # return b       //这里加return则函数会结束


# 结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。
#
# 要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab 函数改写后的第二个版本：

# 没有返回值无法复用

# i = fab_1(5)
# print(i)

def fab_2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    print(sys.getsizeof(L))
    return L


# for n in fab_2(5):        //fab_2(5)返回的是一个列表，n表示列表中每一个值
#    print n

# i = fab_2(5)
# print i

# 改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List 来保存中间结果，而是通过 iterable 对象来迭代

# 每次允许 都需要让L[]参与运算，L[]越大，内存需要越大

class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


# Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数：

# for n in Fab(5):
#   print n

# 然而，使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。如果我们想要保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，yield 就派上用场了：

# 使用 yield 的第四版

def fab_4(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
    print(sys.getsizeof(a))
    print(sys.getsizeof(b))
    print(sys.getsizeof(n))


for n in fab_2(5):
    print n

for n in fab_4(5):
    print n

# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，
# 而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，
# 代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。

# >>> f = fab(5)
# >>> f.next()
# 1
# >>> f.next()
# 1
# >>> f.next()
# 2
# >>> f.next()
# 3
# >>> f.next()
# 5
# >>> f.next()
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# StopIteration


# 当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。
#
# 我们可以得出以下结论：
#
# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
#
# yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
##
# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
#
# 清单 7. 使用 isgeneratorfunction 判断
# 1
# 2
# 3
# >>> from inspect import isgeneratorfunction
# >>> isgeneratorfunction(fab)
# True
# 要注意区分 fab 和 fab(5)，fab 是一个 generator function，而 fab(5) 是调用 fab 返回的一个 generator，好比类的定义和类的实例的区别：
#
# 清单 8. 类的定义和类的实例
# 1
# 2
# 3
# 4
# 5
# >>> import types
# >>> isinstance(fab, types.GeneratorType)
# False
# >>> isinstance(fab(5), types.GeneratorType)
# True
# fab 是无法迭代的，而 fab(5) 是可迭代的：
#
# 1
# 2
# 3
# 4
# 5
# >>> from collections import Iterable
# >>> isinstance(fab, Iterable)
# False
# >>> isinstance(fab(5), Iterable)
# True
