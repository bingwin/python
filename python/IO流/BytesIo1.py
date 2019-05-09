# -*- coding: utf-8 -*-

# python2 暂时没有找到bytesio模块

from cStringIO import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

