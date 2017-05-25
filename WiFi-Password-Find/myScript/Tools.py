#!/usr/bin/python
#coding:utf-8

import ftplib
import os
import sys


#---------- 数组中文乱码 -----------#

# 将 "\\U90fd" 转换 "\u90fd" (数组将 "\\U90fd" 字符串输出为中文，必须转为 "\u90fd" 格式)
def getUnicodeStrFromOther(string):
    if "\\\\U" in string:
        return string.replace("\\\\U","\\u")        
    elif "\\U" in string:
        return string.replace("\\U","\\u")
    return string

# 将 "\u90fd\u662f\u7231\u7684" 转换为中文输出
def getUTF8FromUnicodeStr(unicodeString):
    return unicodeString.decode('unicode_escape').encode('utf-8')

# 将数组中 item 包含 "\\U90fd" 转换 "\u90fd" 
def getItemAtArrayItem(item):
    if "\\U" in item:
        item = getUnicodeStrFromOther(item)
        item = getUTF8FromUnicodeStr(item)
    return item
#---------- 数组中文乱码 -----------#

#---------- Path -----------#
# 获取当前执行文件的路径，相当于 shell 的 bash 中 $0
def getCurrentPath():
    return os.path.dirname(__file__)

# 获取当前执行文件的目录
def getPardir():
    return os.path.abspath(os.path.join(getCurrentPath(), os.pardir))
#---------- Path -----------#

def execute(command):
    return os.popen(command).read()

# 写入文件
def writeToFile(file,text):
    file_object = open(file, "w")
    file_object.write(text)
    file_object.close()
