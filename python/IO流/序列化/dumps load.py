# -*- coding: utf-8 -*-

# import pickle
#
# # python2 序列化后不是bytes  反序列化后是对象
#
# dic = {'age': 23, 'job': 'student'}
# byte_data = pickle.dumps(dic)
# print(byte_data)
# byte_data2 = pickle.loads(byte_data)
# print(byte_data2)


# python3
# >>> import pickle
# >>> d = dict(name='Bob', age=20, score=88)
# >>> pickle.dumps(d)
# b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

# cPickle和pickle。这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。用的时候，先尝试导入cPickle，如果失败，再导入pickle：
import cPickle as pickle
dic = {'age': 23, 'job': 'student'}
byte_data = pickle.dumps(dic)
print(byte_data)
byte_data2 = pickle.loads(byte_data)
print(byte_data2)