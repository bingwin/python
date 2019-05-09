# -*- coding: utf-8 -*-

from cStringIO import StringIO
# from io import StringIO

# write to StringIO:
f = StringIO()
f.write('dasda')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())