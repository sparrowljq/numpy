import numpy as np
# numpy字节交换
# 多字节对象都被存储为连续的字节序列。字节顺序，是跨越多字节的程序对象的存储规则
# 大端模式：指“高位低地址，低位数据高地址” 小端模式：”高位数据高地址，低位数据低地址“
# numpy.ndarray.byteswap() 函数将 ndarray 中每个元素中的字节进行大小端转换

a = np.array([1, 256, 8755], dtype=np.int16)
# print(a)
# 以十六进制表示内存中的数据
# 输出结果为<map object at 0x0000019B96F209C8>
# print(map(hex, a))
# print(a.byteswap(True))
# 输出结果为<map object at 0x0000019B96F209C8>
# print(map(hex, a))

# Numpy副本和视图
# 副本是一个数据的完整拷贝，如果我们对副本进行修改，不会影响到原始数据，物理内存不相同
# 视图是数据的引用，如果对视图修改会改变原始数据
# 视图一般发生在：numpy的切片操作返回原始数据的视图、调用ndarray的view函数产生视图
# 副本：python序列的切片操作、调用deepCopy()函数、调用ndarray的copy函数产生一个副本

# 视图的例子
a = np.arange(6)
# 输出结果[0 1 2 3 4 5]
# print(a)
# 调用id函数
# 输出结果为3217965727376
# print(id(a))
# b是指向a数组的引用
b = a
# 输出结果
# print(b)
# b.shape =3,2
# 输出结果为
# [[0 1]
#  [2 3]
#  [4 5]]
# print(b)
# 输出结果为
# [[0 1]
#  [2 3]
#  [4 5]]
# print(a)
# 用array的view创建视图 b = a.view()

# 创建副本
# ndarray.copy() 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置
a = np.array([[10, 10], [2, 3], [4, 5]])
# print(a)
b = a.copy()
print(b)
# 输出结果为False
# print(a is b)
b[0, 0] = 100
# 输出结果为
# [[100  10]
#  [  2   3]
#  [  4   5]]
# print(b)
# 输出结果为
# [[10 10]
#  [ 2  3]
#  [ 4  5]]
# print(a)

# Numpy矩阵库（Matrix）
# numpy包含了一个矩阵库num.matlib，该模块中的函数返回的是一个矩阵，而不是ndarray对象
# 一个 的矩阵是一个由行（row）列（column）元素排列成的矩形阵列
# 矩阵里的元素可以是数字、符号或数学式。以下是一个由 6 个数字元素构成的 2 行 3 列的矩阵
from numpy import matlib
# 输出结果为
# [[4.60761105e-292 1.13900535e+246]
#  [1.97629389e+166 2.34173968e-258]]
# print(matlib.empty((2, 2)))

# 创建一个零填充矩阵
# 输出结果为
# [[0. 0.]
#  [0. 0.]]
# print(matlib.zeros((2, 2)))

# 创建一个1填充矩阵 numpy.matlib.ones()
# 创建一个对角矩阵 numpy.matlib.eye(n, M,k, dtype) 其中k表示对角线索引
# 输出结果为
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
# print(matlib.eye(n=4, M=4, k=0, dtype=float))
# 输出结果为
# [[0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]
#  [0. 0. 0. 0.]]
# print(matlib.eye(n=4, M=4, k=1, dtype=float))

# numpy.matlib.identity() 函数返回给定大小的单位矩阵
# 输出结果为
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
# print(matlib.identity(5, dtype=float))

# numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的
# 输出结果为
# [[0.70006156 0.2475764  0.26519078]
#  [0.04685052 0.65282257 0.69173617]
#  [0.09618866 0.22751606 0.39577652]]
# print(matlib.rand(3, 3))
# 将ndarray数组转换成n维数组
arr = np.array([[1, 2], [3, 4]])
# 输出结果为
# [[1 2]
#  [3 4]]
# print(np.asmatrix(arr))

