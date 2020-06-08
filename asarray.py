import numpy as np
# 从已有的数组创建数组
# np.asarray(a, dtype = None, order = None)
# a表示日任意形式的参数，可以是，列表、列表的元组，元组，元组的元组，元组的列表，多维数组
# order 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序
x = [1, 2, 3]
# 将列表转换为array
a = np.asarray(x)
# 输出结果为[1 2 3]
# print(a)
# 将元组转换为array
x = (1, 2, 3)
a = np.asarray(x)
# 输出结果为[1 2 3]
# print(a)
# 将元组列表转换为array
# x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
# 输出结果为[(1, 2, 3) (4, 5)]
# print(a)
# 设置dtype参数
x = [1, 2, 3, 4, 5]
a = np.asarray(x, dtype=float)
# 输出结果为[1. 2. 3. 4. 5.]
# print(a)

# numpy.frombuffer 用于实现动态数组 接受buffer输入参数，以流的形式读入转成ndarray对象
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# buffer可以是任意对象，以流的形式读入
# 返回数组的数据类型，可选
# count读取的数据数量，默认为-1，读取所有的数据
# offset读取的起始位置，默认为0
# buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b
s = b'Hello world'
a = np.frombuffer(s, dtype='S1')
# 输出结果为[b'H' b'e' b'l' b'l' b'o' b' ' b'w' b'o' b'r' b'l' b'd']
# print(a)
# numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组
# numpy.fromiter(iterable, dtype, count=-1) count表示读取数据量
list = range(5)
it = iter(list)
a = np.fromiter(it, dtype=float)
# [0. 1. 2. 3. 4.]
print(a)

