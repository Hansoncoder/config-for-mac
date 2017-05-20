## config-for-mac

　　这是我个人使用电脑的一些配置脚本，个人的偏好设置，部分是高效开发使用，部分是个人喜好使用，在此记录方便以后自己查阅。

#### ramDisk.sh

　　这是一个将内存虚拟化为硬盘的脚本，size = 1024M,名字为 ramdisk.主要用于存储 Xcode 编译生成的临时文件，加快重复编译时间。Xcode->Preferences->Locations->Derived Data 修改路径为虚拟化硬盘的路径。
  
#### wifi.command

　　Mac 下查看 WiFi 密码特别不方便，而且我们一般连接上 WiFi 就不去记录 WiFi 密码，当朋友到家里玩的时候，通过各种方式查 WiFi 密码对于一个不懂计算机的人来说比较麻烦。本脚本后缀为.command，其目的是提供给非开发者使用。方便他们双击运行，看到 WiFi 名称和密码。
  
#### iTerm2配色方案

　　为了统一管理，将这些系统配置文件一律放到`~/config-for-mac`目录下。将 solarized 下载下来，拷贝到 `~/config-for-mac` 目录下。
　　打开 iterm　在 Preferences->Profiles->Colors 标签，点击 Load Preset 列表中的 Import 进行导入，然后选择一种即可。
```bash
git clone git://github.com/altercation/solarized.git
```

#### dotfile 配置

　　下载到`~/config-for-mac`目录下，执行命令一键配置。
```bash
git clone https://github.com/mathiasbynens/dotfiles.git
# 进入子目录执行bootstrap脚本
cd dotfiles && source bootstrap.sh
```

#### Aria2 配置

```bash
# chrome网盘助手插件
https://github.com/acgotaku/BaiduExporter.git
# aria2GUI
https://github.com/yangshun1029/aria2gui/releases
```
