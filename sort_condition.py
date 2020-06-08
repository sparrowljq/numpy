import numpy as  np
# 排序、条件刷选函数
# Numpy提供的三种排序方法quicksort(快速排序)、mergesort(归并排序)、heapsort(堆排序)
# numpy.sort(a, axis, kind, order) kind表示排序类型 order:如果数组包含字段，则是要排序的字段
dt = np.dtype([("name", 'S20'), ("age", 'i4')])
b = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype=dt)
# 输出结果为[(b'ravi', 17) (b'raju', 21) (b'anil', 25) (b'amar', 27)]
# print(np.sort(b, kind='quicksort', order='age'))

# numpy.argsort() 函数返回的是数组值从小到大的索引值
x = np.array([3, 1, 2])
# 输出结果为[1 2 0]
# print(np.argsort(x))

# numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，
# 排序时优先照顾靠后的列
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print(ind)
# 使用这个索引获取数据
print([nm[i] +", "+dv[i] for i in ind])
# msort(a)数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)
# sort_complex(a)	对复数按照先实部后虚部的顺序进行排序
# partition(a, kth[, axis, kind, order])	指定一个数，对数组进行分区
# argpartition(a, kth[, axis, kind, order])	可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
res=np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j])
# 输出结果为[1.+2.j 2.-1.j 3.-3.j 3.-2.j 3.+5.j]
# print(res)

# 分区排序
a = np.array([3, 1, 2, 4, 7, 6])
# 输出结果为[1 2 3 4 6 7]
# print(np.partition(a, 4)) # 将数组中所有元素从小到大排列，4表示比第5小的放前面，比第5大的放后面
# 将数组中小于1的放在1的前面，1~3放中间，大于3的放后面
# 输出结果为[1 2 3 4 7 6]
# print(np.partition(a, (1, 3)))

arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
# 输出结果为[  0   1  10  39  57  23  46 120]
# print(np.partition(arr, 2))
# 输出结果为[6 4 5 3 1 2 0 7]
# 找到数组中第三小的索引值 输出结果5
# print(np.argpartition(arr, 2)[2])
# 输出结果为[5 3 2 6 4 0 1 7]
# print(np.argpartition(arr, -2))
# 找出数中第二大的值 输出结果为57
# print(arr[np.argpartition(arr, -2)[-2]])

# numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引
a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
# 输出结果为
# [[30 40 70]
#  [80 20 10]
#  [50 90 60]]
print(a)
# 输出结果为7
print(np.argmax(a))
# 输出结果为[1 2 0]
print(np.argmax(a, axis=0))
# 返回数组中非零元素的索引
# 输出结果为(array([0, 0, 1, 1, 2, 2], dtype=int64), array([0, 1, 1, 2, 0, 2], dtype=int64))
print(np.nonzero(a))

# numpy.where() 函数返回输入数组中满足给定条件的元素的索引
y = np.where(a > 10)
# 输出结果为[30 40 20 50 60]
print(a[y])

# numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素
conditon = np.mod(a,3)==0
# 输出结果为
# [[ True False  True]
#  [ True False False]
#  [False  True  True]]
print(conditon)
# 输出结果为[30  0  0  0 60]
print(np.extract(conditon, a))
