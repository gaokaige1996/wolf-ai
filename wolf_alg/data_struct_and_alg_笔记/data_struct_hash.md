## data_struct_and_alg 笔记 - hash
- **概述：**
>
>
>
>
>
>
>

- **hash表的装载因子：**
>       装载因子：α=(填入表中的元素个数)/(哈希表的长度)
>       装载因子α与填入表中的元素成正比，α越大，表明产生冲突的可能性越大。
>       hash表的平均查找长度是装载因子α的函数，只是不同处理冲突的方法有不同的函数。
>


- **hash表的碰撞两种思路：**
>       1、一个桶中只能放一个元素，对同一个桶内的数据进行线性探测，就是每个桶中只有一个元素，如果发生碰撞，则顺序查找桶后面的桶，将其让如后面没有被使用的桶中
>       2、一个桶中可以放多个元素，然后利用链表或者树等他们数据结构进行组织起来
>

- **哈希碰撞攻击：**
>       构造数据使得所有数据全部碰撞到一个桶中，这样就会导致消耗大量的CPU资源，导致系统无法快速响应请求，从而达到拒绝服务攻击(DoS)的目的。
>       **暴雪的Hash算法**
>

- **应用：**
>       PHP的hash表应用在Array数据类型，还在Zend虚拟机内部用于存储上下文环境信息（执行上下文的变量以及函数均使用哈希表存储结构）
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
>       参考：https://wizardforcel.gitbooks.io/the-art-of-programming-by-july/content/a.4.html     倒排索引关键词不重复Hash编码
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
