#!/usr/bin/python
#coding:utf-8

import ftplib
import os
import sys
import Tools


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
    SSIDListStr = Tools.execute('defaults read /Library/Preferences/SystemConfiguration/com.apple.airport.preferences | grep SSIDString')
    temp = SSIDListStr.replace("SSIDString = ","").replace(";",",")
    tempSSIDList = temp.split(",")
    # 处理查询结果
    if len(tempSSIDList) > 0 :
        tempSSIDList.pop()
    
    # 去除一些无用字符串
    SSIDList = []
    for index,SSIDName in enumerate(tempSSIDList):
        # if (SSIDName.find("\\\\U") == -1): # 去除中文
            SSIDList.append(SSIDName.strip().replace("\"",""))
    return SSIDList;

# 获取 WiFi 密码
def getWiFiPasswd(wifiName) :
    output = os.popen('security find-generic-password -wa ' + wifiName)
    os.system('/usr/bin/osascript ' + Tools.getCurrentPath() + '/window.AppleScript')
    wifiPasswd = output.read()
    return wifiPasswd

# 输出 WiFi 名称
def printWiFIName(List):
    print "----------------------------------"
    for index,item in enumerate(List):
        print "|  " + str(index+1) + '.WiFi名称：' + Tools.getItemAtArrayItem(item)
    print "----------------------------------"

# 写入文件
def writeToFile(file,text):
    file_object = open(file, "w")
    file_object.write(text)
    file_object.close()

def printfResult(ssid,passwd):
    text = "您可能存在以下情况：\n 1.WiFi名称：" + Tools.getItemAtArrayItem(wifiName) + " 没有密码！\n 2.没有配置 window.AppleScript 脚本！"
    if len(passwd) != 0:
        text = "WiFi名称：" + ssid + "\nWiFi密码："+ passwd
    filePath = Tools.getPardir() + "/wifi.txt"
    writeToFile(filePath, text)
    os.popen("open " + filePath)

## -------- 进入主题 ------------- ##

# 获取WiFi名称
SSIDList = getWiFiNameList()
# 读取用户输入
selectIndex = readIndex(SSIDList)

# 通过 WiFi 名称获取WiFi密码
wifiName = SSIDList[selectIndex]
wifiPasswd = getWiFiPasswd(Tools.getItemAtArrayItem(wifiName))

# 写入文件
printfResult(wifiName,wifiPasswd)

## -------- end ------------- ##
