## config-for-mac

　　这是我个人使用电脑的一些配置脚本，个人的偏好设置，部分是高效开发使用，部分是个人喜好使用，在此记录方便以后自己查阅。

#### ramDisk.sh

　　这是一个将内存虚拟化为硬盘的脚本，size = 1024M,名字为 ramdisk.主要用于存储 Xcode 编译生成的临时文件，加快重复编译时间。Xcode->Preferences->Locations->Derived Data 修改路径为虚拟化硬盘的路径。
  
#### wifi.command

　　Mac 下查看 WiFi 密码特别不方便，而且我们一般连接上 WiFi 就不去记录 WiFi 密码，当朋友到家里玩的时候，通过各种方式查 WiFi 密码对于一个不懂计算机的人来说比较麻烦。本脚本后缀为.command，其目的是提供给非开发者使用。方便他们双击运行，看到 WiFi 名称和密码。

　　我用了这个 `wifi.command` ,感觉挺麻烦的，要输入 WiFi 名称、登录账户密码，搞得太麻烦了。现在开发了一个升级版本的，用的是 Python 脚本和 AppleScript 共同完成，Python 用于选择保存过的 WiFi 名称，AppleScript 用于完成登录框自动填充账户密码，点击确定。升级版本的脚本需要在 `AppleScript脚本` 中配置登录用户名和密码(修改`AppleScript脚本` 时，使用脚本编辑器或在VSCode一类的打开，别用文本编辑器打开，有中文会识别错误)

升级版本脚本使用：
>　　1.修改 `AppleScript脚本` yourLoginUserName 为你电脑登录名
　　2.修改 `AppleScript脚本` yourLoginUserPassword 为你电脑登录密码
　　3.双击 `wifi.command` 执行，输入`数字`选择你保存过的 WiFi 名称即可
　　4.如果只查询一次，用第一个版本也还不错。

#### iTerm2配色方案

　　为了统一管理，将这些系统配置文件一律放到`~/config-for-mac`目录下。将 solarized 下载下来，拷贝到 `~/config-for-mac` 目录下。
　　打开 iterm　在 Preferences->Profiles->Colors 标签，点击 Load Preset 列表中的 Import 进行导入，然后选择一种即可。
```bash
git clone git://github.com/altercation/solarized.git
```

　　为了使终端的 ls 针对不同类型文件名称着色，我统一用 dircolors-solarized 配色，将 dircolors-solarized 下载到`~/config-for-mac`目录下。本次设置需要用 GNU Coreutils 替换 Mac 的 ls 命令。
```bash
# 安装 coreutils
brew install coreutils
# 下载 dircolors-solarized
cd ~/config-for-mac
git clone https://github.com/seebi/dircolors-solarized.git
# 配置 .bash_profile
vim ~/.bash_profile
##### 添加如下代码 #####
if brew list | grep coreutils > /dev/null ; then
  PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"
  alias ls='ls -F --show-control-chars --color=auto'
  eval `gdircolors -b $HOME/config-for-mac/dircolors-solarized/dircolors.ansi-dark`
fi
#####     end    #####
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

#### 参考文献
[[译]MAC OS X的命令行技巧](https://crazyof.me/blog/archives/2634.html)
[Awesome OS X Command Line](https://github.com/herrbischoff/awesome-osx-command-line)