# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 类属性对于类的所有实例都是相同的，而实例属性对于每个实例都是特定的。 对于两个不同的实例，将有两个不同的实例属性。
class MyClass(object):
   pass
# Create first instance of MyClass
this_obj = MyClass()
print(this_obj)
# Another instance of MyClass
that_obj = MyClass()
print (that_obj)

class InstanceCounter(object):
   count = 0 # class attribute, will be accessible to all instances
   def __init__(self, val):
      self.val = val
      InstanceCounter.count +=1 # Increment the value of class attribute, accessible through class name
# In above line, class ('InstanceCounter') act as an object
   def set_val(self, newval):
      self.val = newval

   def get_val(self):
      return self.val

   def get_count(self):
      return InstanceCounter.count
a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)


for obj in (a, b, c):
   print ('val of obj: %s' % (obj.get_val()))  # Initialized value ( 9, 18, 27)
   print ('count: %s' % (obj.get_count()))  # always 3


