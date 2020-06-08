import numpy as np
# 数组操作 修改形状、翻转数组、修改数组维度、连接数组、分割数组、数组元素的添加、删除
# numpy.ndarray.flat 是一个数组元素迭代器
x = np.arange(12).reshape(4, 3)
# print(x)
# 遍历结果为0 1 2 3 4 5 6 7 8 9 10 11
# for item in x.flat:
#    print(item, end=" "
# 输出结果为[ 0  1  2  3  4  5  6  7  8  9 10 11]
# for item in np.nditer(x,flags=['external_loop']):
#    print(item, end=" ")
# umpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
# 输出结果 [ 0  1  2  3  4  5  6  7  8  9 10 11]
# print(x.flatten(order='A'))
# 输出结果为
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
# print(x.copy(order='F'))

# numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图
# （view，有点类似 C/C++引用reference的意味），修改会影响原始数组
# 输出结果为[ 0  1  2  3  4  5  6  7  8  9 10 11]
# print(x.ravel())

# 翻转数组
# transpose 对换数组的维度
# 数组转置 ndarry.T
# rollaxis 向后滚动指定的轴
# swapaxes 对换数组的两个轴
# 输出结果

# transpose函数用法
arr = np.arange(15).reshape(3, 5)
# 输出结果
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
# print(arr)
# 矩阵的转置相当于将轴0,1交换
# 输出结果为
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]
# print(arr.transpose(1, 0))

# 三维数组的交换
arr = np.arange(24).reshape(2, 3, 4)
# print(arr)
# 表示将1轴和0轴交换，2轴不变
# print(arr.transpose(1, 0, 2))

# print(np.transpose(arr))

