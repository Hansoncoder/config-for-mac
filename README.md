# config-for-mac

　　这是我个人使用电脑的一些配置脚本，个人的偏好设置，部分是高效开发使用，部分是个人喜好使用，在此记录方便以后自己查阅。

- ramDisk.sh
　　这是一个将内存虚拟化为硬盘的脚本，size = 1024M,名字为ramdisk.主要用于存储Xcode编译生成的临时文件，加快重复编译时间。Xcode->Preferences->Locations->Derived Data修改路径为虚拟化硬盘的路径。