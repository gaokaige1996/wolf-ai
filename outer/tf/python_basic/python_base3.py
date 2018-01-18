#coding=utf-8

def func1():
    from distutils.core import setup, Extension
    pass


def func2():
    """
    控制小数位的输出
    """
    from decimal import Decimal
    a = 52348.23459734957345979
    b = 1.111111111111
    print(a)
    print('%.2f'%a)
    print(Decimal(a).quantize(Decimal('0.00')))

    #精度控制
    print('{0:.3f}'.format(a,b))
    #其中.2表示长度为2的精度，f表示float类型
    print('{:.2f}'.format(321.33345))
    #控制宽度
    print('{0:4}{1:3}'.format('abc', 'python'))

def func3():
    """
    线程设置：
        join:
            join() 代表主线程要等待子线程执行完再继续执行（被阻塞），期间是无法执行的
            用 Ctrl+C 试验可知，当使用了 join() 时，主线程不能及时接收到退出信号。要等子线程都执行完，才会处理退出信号
            所以使用join后，子线程不能及时处理Ctrl+C的信号
        setDaemon：
            setDaemon(True) 代表让子线程跟随主线程销毁
    信号：
        信号 SIGINT，代表 Ctrl+C 或 pm2 的 stop。信号 SIGTERM，代表 kill命令 或 pm2 的 kill
    """
    import threading,time,signal,sys

    def printa():
        while True:
            print('printa')
            time.sleep(1)
    def printb():
        while True:
            print('printb')
            time.sleep(1)
    def quit(signum,frame):
        print('program quit')
        sys.exit()

    #设置信号
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)

    a = threading.Thread(target=printa)
    b = threading.Thread(target=printb)
    a.start()
    b.start()

    flag = 0
    if flag:
        a.join()
        b.join()
    else:
        a.setDaemon(True)
        b.setDaemon(True)


if __name__ == '__main__':
    #func1()
    #func2()
    func3()