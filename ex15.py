# -*- coding: utf-8 -*-

#import 语句，将python的特性引入脚本
from sys import argv
#解包，将argv的参数分别存到下面的每一个变量
script, filename = argv
#将filename对应的文件对象存到txt
txt = open(filename)
#打印我所输入的文件名
print "here's your file %r:" % filename
#使用文件对象的一个方法
print txt.read()
#打印
print "type the filename again:"
#初始化用户输入为>
file_again = raw_input(">")
#将file_again的文件
txt_again = open(file_again)
#打印
print txt_again.read()
