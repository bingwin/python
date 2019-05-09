# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter

# pattern = re.compile(r'\d+')  # 查找数字
pattern = re.compile(r':" \d+ google')  # 查找数字

result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob:" 123 google:" 456 google456')

print(result1)
print(result2)

#提取邮件地址、url
import re
text = "Please contact us at contact@qq.com for further information."+\
        " You can also give feedbacl at feedback@yiibai.com"


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print emails


line ="Now a days you can learn almost anything by just visiting http://www.google.com. " \
      "But if you are completely new to computers or internet then first you need to leanr those"

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
print(urls)

