#!/bin/bash
echo -e "请输入WiFi名称,输入完成按回车"
read wifiName
if [[ $wifiName == "" ]];
then
  wifiName="wifiName"
fi

wifiPasswd=`security find-generic-password -wa $wifiName`
echo $wifiPasswd

if [[ $wifiPasswd == "" ]];
 then
   echo -e "* * * * * * *\n您输入的WiFi名称为: $wifiName\n\n输入WiFi名称错误或者未保存到电脑\n请查看本电脑连接的WiFi名称重新执行输入\n* * * * * * *" > wifi.txt && open ./wifi.txt
 else
   echo -e "WiFi账户: $wifiName \nWiFi密码: $wifiPasswd" > wifi.txt && open ./wifi.txt
 fi
