## NLP_ML - 谱聚类
- **概述：**
>       谱聚类算法最初用于计算机视觉、VLSI设计等领域,最近才开始用于机器学习中,并迅速成为国际上机器学习领域的研究热点。
>       谱聚类算法建立在图论中的谱图理论基础上,其本质是将聚类问题转化为图的最优划分问题,是一种点对聚类算法。
>
>       比起传统的k-means算法，谱聚类对数据分布的适应性更强，聚类效果也很优秀，同时聚类的计算量也小很多，实现起来也不复杂。
>       谱聚类在最近几年变得受欢迎起来，主要原因就是它实现简单，聚类效果经常优于传统的聚类算法（如K-Means算法）。
>       如果掌握了谱聚类算法，会对矩阵分析，图论和降维中的主成分分析等有更加深入的理解。
>
>
>       首先根据给定的样本数据集定义一个描述成对数据点相似度的亲合矩阵,并计算矩阵的特征值和特征向量,然后选择合适的特征向量聚类不同的数据点。
>

- **谱聚类：**
>       谱聚类是图论中演化出来的算法。
>
>       思想：
>           主要思想是把所有数据看成空间的点，这些点之间可以用边连接起来。距离较远的两个点之间的边权重值较低，而距离较近的两个点之间的边权重值较高，
>           通过对所有数据点组成的图进行切图，让切图后不同的子图间边权重和尽可能的低，而子图内的边权重和尽可能的高，从而达到聚类的目的。
>
>       谱聚类是一种基于图论的聚类方法，通过对样本数据的拉普拉斯矩阵的特征向量进行聚类，从而达到对样本数据聚类的目的。
>           谱聚类可以理解为将高维空间的数据映射到低维，然后在低维空间用其它聚类算法（如KMeans）进行聚类。
>
>       要理解谱聚类，需要对图论中的无向图，线性代数和矩阵分析都有一定了解。
>
>

- **DBSCAN密度聚类：**
>       DBSCAN密度聚类是一种很典型的密度聚类算法，k-means、BIRCH这些一般只适用于凸样本集的聚类相比，DBSCAN密度聚类既可以用于凸样本集，也可以适用于非凸样本集。
>
>       DBSCAN密度聚类是一种基于密度的积累算法，这类算法一般假定类别可以通过样本分布的紧密程度决定。
>           同一类别的样本，他们之间的紧密相连的，也就是说，在该类别任意样本周围不远处一定有同类别的样本存在。
>           将紧密相连的样本划为一类，这样就得到了一个聚类类别。
>
>       DBSCAN算法特点：
>           DBSCAN算法不是完全稳定的算法，可以通过多次计算选择最优值。
>
>       工程优化点：
>           如果样本量较大，则一般采用KD树或者球树来快速的搜索最近邻
>
>       DBSCAN vs k-Means：
>           DBSCAN最大的不同就是不需要输入类别数k，而且最大的优势是可以发现任意形状的聚类簇，而不像k-Means仅仅适用于凸的样本集聚类。
>           同时他在聚类的同时还可以找出异常点。
>
>       异常点处理：
>           DBSCAN算法一般将离群点样本点标记为噪音点
>
>       应用场景：
>           如果数据集是稠密的，而且数据集不是凸的，那么用DBSCAN会比k-Means效果好。
>           如果数据集不是稠密的，不推荐使用DBSCAN来聚类
>
>
>


- **待续：**
>       参考：https://blog.csdn.net/qq_24519677/article/details/82291867   谱聚类（Spectral Clustering）算法介绍
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
>
>
>
>
>
>
>
