#!/usr/bin/python
#coding:utf-8

import ftplib
import os
import sys
import Tools

# 获取 WiFi 密码
def getWiFiPasswd(wifiName) :
    output = os.popen("security find-generic-password -wa " + wifiName)
    os.system("/usr/bin/osascript " + Tools.getCurrentPath() + "/window.AppleScript")
    wifiPasswd = output.read()
    return wifiPasswd

def printfResult(ssid,passwd):
    text = "您的WiFi名称：" + Tools.getItemAtArrayItem(wifiName) + " 包含中文！\n 请用 wifi.command 查看其他 WiFi 密码！"
    if len(passwd) != 0:
        text = "WiFi名称：" + ssid + "\nWiFi密码："+ passwd
    filePath = Tools.getPardir() + "/wifi.txt"
    Tools.writeToFile(filePath, text)
    os.popen("open " + filePath)


wifiName = Tools.execute("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'")
wifiName = wifiName.strip()
wifiPasswd = getWiFiPasswd(wifiName)
printfResult(wifiName,wifiPasswd)