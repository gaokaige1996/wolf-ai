## media-audio ctc（Connectionist temporal classification）
- **概述：**
>       目前主流的语音识别都大致分为特征提取，声学模型，语音模型
>       目前结合神经网络的端到端的声学模型训练方法主要CTC和基于Attention两种
>
>       CTC是计算一种损失值，主要的优点是可以对没有对齐的数据进行自动对齐，主要用在没有事先对齐的序列化数据训练上。
>
>       适合于输入特征和输出标签之间对齐关系不确定的时间序列问题,CTC可以自动端到端地同时优化模型参数和对齐切分的边界。！！！
>
>       在序列学习问题中，模型的预测过程本质是一个空间搜索过程，也称为解码，如何在限定的时间条件下搜索到最优解是一个非常有挑战的问题。！！！
>
>

- **ctc的特点：**
>       传统的Framewise训练需要进行语音和音素发音的对齐，比如“s”对应的一整段语音的标注都是s；而CTC引入了blank（该帧没有预测值），“s”对应的一整段语音中只有一个spike（尖峰）被认为是s，
>           其他的认为是blank。对于一段语音，CTC最后的输出是spike的序列，不关心每一个音素对应的时间长度。
>

- **CTC优缺点：**
>       优点：
>           1、可迁移性比较好。比如朋友之间的聊天和正式发言之间的差异较大，但它们的声学模型却是类似的。
>           2、CTC是单调对齐的。这在语音识别上是没啥问题的，但在机器翻译的时候，源语言和目标语言之间的语序不一定一致，也就不满足单调对齐的条件。
>           3、CTC的输入/输出是many-to-one的，不支持one-to-one或one-to-many。比如，“th”在英文中是一个音节对应两个字母，这就是one-to-many的案例。
>           4、Y的数量不能超过X，否则CTC还是没法work
>       缺点：
>           1、条件独立的假设太强，与实际情况不符，因此需要语言模型来改善条件依赖性，以取得更好的效果
>           假设在给定输入序列和模型参数，RNN每一时刻的输出之间是条件独立的。 ！！！
>
>       如果在语音识别中，能够结合语言模型的话，将可以极大的改善语音识别的准确率。这种情况下的CTC loss为：略
>

- **CTC推断：**
>       CTC的正向推断（Inference），由于对齐有很多种可能的情况，采用穷举法是不现实的。
>

- **CTC：**
>       神经网络+CTC的结构除了可以应用到语音识别的声学模型训练上以外，也可以用到任何一个输入序列到一个输出序列的训练上（要求：输入序列的长度大于输出序列）。！！！
>
>       CTC是一种损失函数，它用来衡量输入的序列数据经过神经网络之后，和真实的输出相差有多少。！！！
>
>       传统的语音识别的声学模型训练，对于每一帧的数据，需要知道对应的label才能进行有效的训练，在训练数据之前需要做语音对齐的预处理。
>           而语音对齐的过程本身就需要进行反复多次的迭代，来确保对齐更准确，这本身就是一个比较耗时的工作。
>
>       CTC模型：
>           与传统的声学模型训练相比，采用CTC作为损失函数的声学模型训练，是一种完全端到端的声学模型训练，不需要预先对数据做对齐，只需要一个输入序列和一个输出序列即可以训练。
>               这样就不需要对数据对齐和一一标注，并且CTC直接输出序列预测的概率，不需要外部的后处理。
>           既然CTC的方法是关心一个输入序列到一个输出序列的结果，那么它只会关心预测输出的序列是否和真实的序列是否接近（相同），
>               而不会关心预测输出序列中每个结果在时间点上是否和输入的序列正好对齐
>
>           CTC引入了blank（该帧没有预测值），每个预测的分类对应的一整段语音中的一个spike（尖峰），其他不是尖峰的位置认为是blank。
>               对于一段语音，CTC最后的输出是spike（尖峰）的序列，并不关心每一个音素持续了多长时间。
>               进过CTC预测的序列结果在时间上可能会稍微延迟于真实发音对应的时间点，其他时间点都会被标记会blank。
>
>           神经网络+CTC应用：
>               神经网络+CTC的结构除了可以应用到语音识别的声学模型训练上以外，也可以用到任何一个输入序列到一个输出序列的训练上（要求：输入序列的长度大于输出序列）
>               比如，OCR识别也可以采用RNN+CTC的模型来做
>                   将包含文字的图片每一列的数据作为一个序列输入给RNN+CTC模型，输出是对应的汉字，因为要好多列才组成一个汉字，所以输入的序列的长度远大于输出序列的长度。
>                   而且这种实现方式的OCR识别，也不需要事先准确的检测到文字的位置，只要这个序列中包含这些文字就好了。
>

- **RNN+CTC模型的训练：**
>       在语音识别中，RNN+CTC模型的训练详细过程，到底RNN+CTC是如何不用事先对齐数据来训练序列数据的。
>       CTC是一种损失函数，它用来衡量输入的序列数据经过神经网络之后，和真实的输出相差有多少。
>
>       比如输入一个200帧的音频数据，真实的输出是长度为5的结果。 经过神经网络处理之后，出来的还是序列长度是200的数据。
>           比如有两个人都说了一句nihao这句话，他们的真实输出结果都是nihao这5个有序的音素，但是因为每个人的发音特点不一样，有的人说的快有的人说的慢，
>           原始的音频数据在经过神经网络计算之后，第一个人得到的结果可能是：nnnniiiiii...hhhhhaaaaaooo(长度是200)，第二个人说的话得到的结果可能是：niiiiii...hhhhhaaaaaooo(长度是200)。
>       这两种结果都是属于正确的计算结果，可以想象，长度为200的数据，最后可以对应上nihao这个发音顺序的结果是非常多的。
>
>       CTC就是用在这种序列有多种可能性的情况下，计算和最后真实序列值的损失值的方法。
>

- **CTC的核心思路：**
>       1、它扩展了RNN的输出层，在输出序列和最终标签之间增加了多对一的空间映射，并在此基础上定义了CTC Loss函数
>       2、借鉴了HMM（Hidden Markov Model）的Forward-Backward算法思路，利用动态规划算法有效地计算CTC Loss函数及其导数，从而解决了RNN端到端训练的问题
>       3、结合CTC Decoding算法RNN可以有效地对序列数据进行端到端的预测
>

- **CTC解码：**
>       在序列学习问题中，模型的预测过程本质是一个空间搜索过程，也称为解码，如何在限定的时间条件下搜索到最优解是一个非常有挑战的问题。！！！
>
>       对CTC网络进行Decoding解码本质过程是选取条件概率最大的输出序列
>       CTC网络的输出序列只对应了搜索空间的一条路径，一个最终标签可对应搜索空间的N条路径，所以概率最大的路径并不等于最终标签的概率最大，即不是最优解。
>
>       常见的CTC解码算法：
>           1、CTC Prefix Search Decoding
>               Prefix Search Decoding是基于前缀概率的搜索算法，它能确保找到最优解，但最坏情况下耗时可能会随着序列长度呈指数增长；
>               Prefix Search Decoding本质是贪心算法，每一次搜索都会选取“前缀概率”最大的节点扩展，直到找到最大概率的目标label，
>                   它的核心是利用动态规划算法计算“前缀概率”。
>           2、CTC Beam Search Decoding
>               CTC Beam Search Decoding是一种Beam Search算法，它能在限定时间下找到近似解，但不保证一定能找到最优解。
>

- **原理详解：**
>       将yts计算了两次，所以除以yts表示的就是t时刻生成ls的约束下，整条label生成的概率：(α*β)/yts
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
>       参考：https://cloud.tencent.com/developer/article/1122128?fromSource=waitui   语音识别中的CTC算法的基本原理解释
>           https://x-algo.cn/index.php/2017/05/31/2345/    CTC原理
>           https://blog.csdn.net/u013193788/article/details/83623444   序列模型之CTC算法
>           https://zhuanlan.zhihu.com/p/21344595   端到端的OCR：验证码识别（理解CTC）
>           https://xiaodu.io/ctc-explained/    CTC Algorithm Explained Part 1：Training the Network（CTC算法详解之训练篇）（5部分详解ctc）
>           https://sunnycat2013.gitbooks.io/blogs/content/posts/ctc/learning-ctc.html  Connectionist Temporal Classification
>           https://blog.csdn.net/luodongri/article/details/77005948    白话CTC(connectionist temporal classification)算法讲解
>           https://www.zhihu.com/question/47642307     谁给讲讲语音识别中的CTC方法的基本原理？
>           https://zhuanlan.zhihu.com/p/27593978   end-to-end语音识别--ctc
>           https://blog.csdn.net/Left_Think/article/details/76370453   语音识别：深入理解CTC Loss原理
>           https://zhuanlan.zhihu.com/p/33464788?edition=yidianzixun&utm_source=yidianzixun&yidian_docid=0IHnKxdI  基于CTC的语音识别基础与实现
>           https://www.jianshu.com/p/e458975a8f14  （CTC解码）Modeified prefix-search decoding algorithm
>           https://blog.csdn.net/JackyTintin/article/details/81251591      Sequence Transducer
>
>
>
>
>
>
