## linux - linux文件
- **概述：**
>       linux文件在磁盘上，只要有(主设备号、次设备号、inode)三个元素，就可以确定一个文件
>       命令stat：
>           列出文件大小，文件所占的块数，块的大小，主设备号和次设备号，inode number，链接数，访问权限，uid,gid,atime,mtime,ctime
>       如：
>       stat go
>          文件："go"
>          大小：3657       块：8          IO 块：4096   普通文件
>        设备：802h/2050d   Inode：13137033    硬链接：1
>        权限：(0775/-rwxrwxr-x)  Uid：( 1000/ruanyang)   Gid：( 1000/ruanyang)
>        最近访问：2016-07-27 19:12:39.792720377 +0800
>        最近更改：2016-07-27 19:11:35.608719535 +0800
>        最近改动：2016-07-27 19:11:35.632719536 +0800
>        创建时间：-
>
>       ll /dev
>       可以查看到，前面第一个字符为c 的表示字符设备，在字符设备里，有主设备号和次设备号，前面的为主设备号，后面的为次设备号
>

- **fcntl设置文件描述符：**
>       fcntl(fd, F_SETFD, FD_CLOEXEC);
>           这里设置为FD_CLOEXEC表示当程序执行exec函数时本fd将被系统自动关闭,表示不传递给exec创建的新进程, 如果设置为fcntl(fd,F_SETFD, 0);那么本fd将保持打开状态复制到exec创建的新进程中
>
>
>
>
>
>
>
>
>
>
>

- **待续：**
>       参考：
>       https://www.ibm.com/developerworks/cn/linux/l-cn-fanotify/index.html    fanotify 监控文件系统
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
