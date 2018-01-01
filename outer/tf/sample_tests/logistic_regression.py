#coding=utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
minist = input_data.read_data_sets('./data', one_hot=True)

def logistic_func1():
    learn_rate = 0.01
    epoch_times = 500
    display_step = 20

    #定义批梯度下降次数，每100张图计算一次梯度
    batch_size = 100

    X = tf.placeholder(tf.float32, shape=[None,784])
    Y = tf.placeholder(tf.float32, shape=[None, 10])

    W = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))

    # 返回一个10维矩阵
    # 注意X,W前后顺序 [None,784]*[784,10]=[None,10]
    pred = tf.nn.softmax(tf.matmul(X, W)+b)

    '''
    tf.reduce_sum(-Y * tf.log(pred), 1) 返回每个实例的交叉熵(向量)，1代表水平方向求和
    tf.reduce_mean() 返回所有交叉熵的平均值(实数)
    '''
    loss = tf.reduce_mean(tf.reduce_sum(-Y * tf.log(pred), 1))

    optimizer = tf.train.GradientDescentOptimizer(learn_rate).minimize(loss=loss)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(epoch_times):
            #批量梯度下降 返回总批量次数(55000/100=550)
            batch_number =int(minist.train.num_examples/batch_size)
            train_cost = 0
            for i in range(batch_number):
                batch_Xs, batch_Ys = minist.train.next_batch(batch_size)
                _,batch_cost = sess.run([optimizer,loss], feed_dict={X:batch_Xs,Y:batch_Ys})
                train_cost += batch_cost/batch_number
            if (epoch + 1) % display_step == 0:
                print('epoch : %04d '%(epoch+1), 'train_cost : {:9f}'.format(train_cost))
        print('Optimization finished')

        # tf.arg_max(pred,1):得到向量中最大数的下标，1代表水平方向
        # tf.equal():返回布尔值，相等返回1，否则0
        # 最后返回大小[none,1]的向量，1所在位置为布尔类型数据
        correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(Y, 1))
        # tf.cast():将布尔型向量转换成浮点型向量
        # tf.reduce_mean():求所有数的均值
        # 返回正确率：也就是所有为1的数目占所有数目的比例
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        #输入正确率
        print("train accuracy : ", sess.run(accuracy, feed_dict={X:minist.train.images, Y:minist.train.labels}))
        print("test accuracy : ", sess.run(accuracy, feed_dict={X:minist.test.images, Y:minist.test.labels}))

if __name__ == '__main__':
    logistic_func1()
