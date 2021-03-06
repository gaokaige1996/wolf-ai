## linux - 网络 - TCP连接的关闭
- **概述：**
>       TCP连接的关闭有两个方法：
>           close
>           shutdown
>       TCP关闭连接的常见问题：
>           1、关闭连接在多线程和多进程共享socket时，有什么区别？
>           2、关闭连接时，有未处理的消息和未发送的消息怎么处理？
>           3、so_linger功能的用处在哪儿？
>           4、对于监控socket执行关闭，和对处于ESTABLISH这种通讯的socket执行关闭，有什么区别？
>
>
>
>
>

- **TCP的close关闭**
>       close的函数调用链：（从上到下）
>           sys_close
>           filp_close
>           fput
>               （仅当socket引用计数为0才会继续向下调用）
>               创建线程时，线程间共享文件描述符，文件描述符引用计数不会增加；
>               创建进程时，会把进程打开的所有文件描述符的引用计数加1；
>               多进程中共享的同一个socket必须都调用了close才会真正的关闭连接
>           __fput
>           sock_close
>           sock_release
>           inet_release
>           tcp_close
>

- **TCP的shutdown关闭：**
>       shutdown的调用链：（从上到下）
>           sys_shutdown
>           inet_shutdown
>           tcp_shutdown
>       shutdown没有引用计数的逻辑，只要调用了就直接关闭连接，所以shutdown与多线程、多进程无关
>
>

- **TCP连接的三次握手：**
>       客户端打开接收和发送功能
>       服务器认可并也打开接收和发送功能
>       客户端确认
>
>

- **TCP连接的关闭的四次握手：**
>       主动端关闭了发送的功能
>       被动端认可
>       被动端关闭发送的功能
>       主动端认可
>
>       对于异常的连接关闭：
>           关闭半连接（即没有完成三次握手的连接），不能发FIN包（即正常的四次握手关闭连接），而是发送RST复位标志去关闭请求，这样半连接的close任务就完成了。
>

- **关闭连接时的未处理接收数据或发送数据：**
>       1、close
>           调用close时，可能导致发送RST复位关闭连接：例如有未读消息、打开so_linger但l_linger却为0、关闭监听句柄时半打开的连接；
>               更多的会发送FIN来四次握手关闭连接，但打开so_linger可能导致close阻塞住等待着对方的ACK表明收到了消息。
>           close关闭连接有三种情况：
>               a、关闭监听句柄
>               b、关闭普通的ESTABLISH状态的连接（未设置so_linger）
>                   有未处理的消息：
>                       在调用close时，如果有未处理的消息，是要丢弃消息的，但是远端误以为发出的消息已经被处理（ACK确认过了），但是实际上未处理，
>                       此时不能发送FIN包，而是会向远端发送一个RST非正常复位关闭连接。
>                       所以要求在关闭连接时候，要确保已经接收、处理了连接上的消息。！！！！
>                   有未发送的消息：
>                       如果有未发送的消息，则尽力保证这些消息都发送出去，会在最后一个报文中加入FIN标志。同时关闭减小网络中小报文的angle算法。
>                       如果没有未发送的消息，则构造一个报文，仅含有FIN标志位，发送出去关闭连接。
>               c、关闭设置了so_linger的连接
>       2、shutdown
>           shutdown有3个参数，分别为：只关闭写、只关闭读、同时关闭读写
>           a、关闭监听句柄
>               关闭读：不再接收新的连接，把端口上的半连接使用RST关闭，与close一样
>               关闭写：没有任何意义
>           b、关闭半连接，发送RST来关闭
>           c、关闭正常连接
>               关闭读：与对端没有任何关系，只是把本机的消息丢掉，我们调用read方法就不起作用了
>               关闭写：与close一样，发出FIN包，告诉对方，本机不再发送消息
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
>       参考：https://blog.csdn.net/yusiguyuan/article/details/24670989
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
>
