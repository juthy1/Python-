# -*- coding: utf-8 -*-
#将变量传递给脚本
#from sys import argv
from sys import argv
#脚本、文件名为参数变量
#script, filename = argv
script, filename = argv

#打印“我们将建立filename的文件”%格式化字符，%r。字符串是你想要展示给别人或者从
#从程序里“导出”的一小段字符。
#print ("We're going to erase %r." % filename)
print ("We're going to erase %r." % filename)
#打印提示，如何退出，确定回车
#print ("If you don't want that, hit CTRL-C (^C).")
print ("If you don't want that, hit CTRL-C (^C).")

#print ("If you do want that, hit RETURN.")
print ("If you do want that, hit RETURN.")
#输入，用？来提示
input("?")

#print ("Opening the file...")
print ("Opening the file...")
#打开文件，‘W’目前还不懂
#target = open(filename, 'w')
target = open(filename, 'w')
#清空文件
#print ("Truncating the file. Goodbye!")
print ("Truncating the file. Goodbye!")
#清空文件的命令truncate()
#target.truncate()
target.truncate()

#打印，现在我将请求你回答这三行
#print ("Now I'm going to ask you for three lines.")
print ("Now I'm going to ask you for three lines.")
#第一行输入
#line1 = input("line 1: ")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#打印，我把这些写入文件
print ("I'm going to write these to the file.")

#target.write(line1, "\n" line2, "\n" line3, "\n")这个是错的
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("I'm going to write these to the file.")
print ("And finally, we close it.")
target.close()
