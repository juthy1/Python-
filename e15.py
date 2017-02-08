# -*- coding: utf-8 -*-
#将变量传递给脚本的方法，import是入口的意思，将系统引入argv 参数变量
from sys import argv

#脚本和文件名为参数变量
script, filename = argv
#txt打开open文件file
txt = open(filename)
#打印”你有一个文件”
print ("Here's your file %r:" % filename)

#打印 txt调用了一个函数接受命令的方式是使用“.”
#紧跟着命令，“嘿，txt！执行你的read命令，无需任何参数！”
print (txt.read())

#这之后就是重复练习，加深印象，再次打印
print ("I'll also ask you to type it again:")
#再次输入一个文件名
file_again = input("> ")

#定义打开上面输入的文件名
txt_again = open(file_again)
#打印执行命令，读取文件
print (txt_again.read())
