#!/usr/bin/python
#coding:utf-8

import ftplib
import os
import sys

def getCurrentPath():
    return os.path.dirname(__file__)

def getPardir():
    return os.path.abspath(os.path.join(getCurrentPath(), os.pardir))

def execute(command):
    return os.popen(command).read()

# 读取整数
def readInt():
    readText = raw_input()
    while (bool(readText.isdigit()) != True) :
        readText = raw_input("输入错误，请重新输入！！\n")
    return int(readText)

# 读取指定范围 [1,lenght] 的整数
def readIndex(SSIDList):
    # 显示 WiFi 列表
    printWiFIName(SSIDList)

    # 获取输入
    lenght = len(SSIDList)
    print "* 请输入你要查询的WiFi编号！！"
    readIndex = readInt()
    while readIndex < 1 or readIndex > lenght :
        print "* 输入错误，请重新输入！！"
        readIndex = readInt()
    return readIndex-1

# 获取 WiFi 名称
def getWiFiNameList():
    SSIDListStr = execute('defaults read /Library/Preferences/SystemConfiguration/com.apple.airport.preferences | grep SSIDString')
    temp = SSIDListStr.replace("SSIDString = \"","").replace("\";",",")
    SSIDList = temp.split(",")
    # 处理查询结果
    if len(SSIDList) > 0 :
        SSIDList.pop()
    for index,SSIDName in enumerate(SSIDList):
        SSIDList[index] = SSIDName.strip()
    return SSIDList;

# 获取 WiFi 密码
def getWiFiPasswd(wifiName) :
    output = os.popen('security find-generic-password -wa ' + wifiName)
    os.system('/usr/bin/osascript ' + getCurrentPath() + '/window.AppleScript')
    wifiPasswd = output.read()
    return wifiPasswd

# 输出 WiFi 名称
def printWiFIName(SSIDList):
    print "----------------------------------"
    for index,SSIDName in enumerate(SSIDList):
        print "|  " + str(index+1) + '.WiFi名称：' + SSIDName
    print "----------------------------------"

# 写入文件
def writeToFile(file,text):
    file_object = open(file, "w")
    file_object.write(text)
    file_object.close()

def printfResult(ssid,passwd):
    text = "WiFi名称：" + wifiName + " 不存在，请选择其他WiFi试试！"
    if len(passwd) != 0:
        text = "WiFi名称：" + ssid + "\nWiFi密码："+ passwd
    filePath = getPardir() + "/wifi.txt"
    writeToFile(filePath, text)
    os.popen("open " + filePath)

## -------- 进入主题 ------------- ##

# 获取WiFi名称

SSIDList = getWiFiNameList()
# 读取用户输入
selectIndex = readIndex(SSIDList)

# 通过 WiFi 名称获取WiFi密码
wifiName = SSIDList[selectIndex]
wifiPasswd = getWiFiPasswd(wifiName)

# 写入文件
printfResult(wifiName,wifiPasswd)
