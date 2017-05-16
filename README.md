## config-for-mac

　　这是我个人使用电脑的一些配置脚本，个人的偏好设置，部分是高效开发使用，部分是个人喜好使用，在此记录方便以后自己查阅。

#### ramDisk.sh

　　这是一个将内存虚拟化为硬盘的脚本，size = 1024M,名字为 ramdisk.主要用于存储 Xcode 编译生成的临时文件，加快重复编译时间。Xcode->Preferences->Locations->Derived Data 修改路径为虚拟化硬盘的路径。
  
#### wifi.command

　　Mac 下查看 WiFi 密码特别不方便，而且我们一般连接上 WiFi 就不去记录 WiFi 密码，当朋友到家里玩的时候，通过各种方式查 WiFi 密码对于一个不懂计算机的人来说比较麻烦。本脚本后缀为.command，其目的是提供给非开发者使用。方便他们双击运行，看到 WiFi 名称和密码。