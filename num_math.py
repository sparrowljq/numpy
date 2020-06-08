# numpy数学函数
# numpyt提供的标准的三角函数有sin()、cos()、tan()
import numpy as np
a = np.array([0, 30, 45, 60, 90])
# 输出结果为[0.         0.5        0.70710678 0.8660254  1.        ]
print(np.sin(a*np.pi/180))

# 算术函数
# Numpy的算术函数包含简单的加减乘除：add、subtract、multiply、divide
# 说明数组必须具有相同的形状或符合数组广播规则

a = np.arange(9).reshape(3, 3)
# print(a)
b = np.array([10, 10, 10])
# 输出结果为
# [[10. 11. 12.]
#  [13. 14. 15.]
#  [16. 17. 18.]]
# print(np.add(a, b))

# numpy.reciprocal() 函数返回参数逐元素的倒数
# print(np.deprecate(a))
a = np.array([0.25,  1.33,  1,  100])
# print(np.reciprocal(a))

# numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
a = np.array([10, 100, 1000])
# 输出结果[    100   10000 1000000]
# print(np.power(a, 2))
b = np.array([1, 2, 3])
# 输出结果为[        10      10000 1000000000]
# print(np.power(a, b))
# numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
# 输出结果为[1 0 2]
# print(np.mod(a, b))
# 输出结果为[1 0 2]
# print(np.remainder(a, b))

# 统计函数
# Numpy提供了很多统计函数，用于从数组中查找最小元素、最大元素、百分位标准差和方差等
# numpy.amin和numpy.amax
# numpy.amin 用于计算数组中的元素沿指定轴的最小元素
# numpy.amax() 用于计算数组中的元素沿指定轴的最大值

a = np.array([[3, 7, 5], [8, 4, 5], [2, 4, 9]])
# print(a)
# 输出结果为：[3 4 2]
# print(np.amin(a, 1))

# numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）
# 输出结果为7
# print(np.ptp(a))

# 沿轴调用
# print(a)
# 输出结果为[4 4 7]
# print(np.ptp(a, axis=1))

# 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。 函数numpy.percentile()接受以下参数
# numpy.percentile(a, q, axis)
# a:输入数组 q:要计算的百分位数，在0~100之间
# axis:沿着计算百分位数的轴

a = np.array([[10, 7, 4], [3, 2, 1]])
# print(a)
# 输出结果为3.5
# print(np.percentile(a, 50))
# axis 为 1，在横行上求
# 输出结果为[7. 2.]
# print(np.percentile(a, 50, axis=1))
# 保持维度不变
# 输出结果
# [[7.]
#  [2.]]
# print(np.percentile(a, 50, axis=1, keepdims=True))

# 为numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
# 输出结果为
# [[30 65 70]
#  [80 95 10]
#  [50 90 60]]
# print(a)
# print(np.median(a))
# 输出结果为[65. 80. 60.]
# print(np.median(a, axis=1))
# 计算平均数
# 输出结果为61.111111111111114
# print(np.mean(a))
# 求加权平均数
a = np.array([1, 2, 3, 4])
wts = np.array([4, 3, 2, 1])
# 输出结果为2.0
print(np.average(a, weights=wts))
# 如果returned=True表示返回权重的和
print(np.average(a, weights=wts, returned=True))

# 标准差是一组数据平均值分散程度的一种度量。
# 标准差是方差的算术平方根。
# std = sqrt(mean((x - x.mean())**2))
# 输出结果为1.118033988749895
# print(np.std([1, 2, 3, 4]))

# 统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，
# 即 mean((x - x.mean())** 2)。
# 换句话说，标准差是方差的平方根。
# 输出结果为1.25
# print(np.var([1, 2, 3, 4]))

# 舍入函数
a = np.array([1.0,5.55,  123,  0.567,  25.532])
# 表示保留一位小数
# print(np.around(a, decimals=1))

# 向下取整
# 输出结果为[  1.   5. 123.   0.  25.]
# print(np.floor(a))
# 向上取整
# 输出结果为[  1.   6. 123.   1.  26.]
# print(np.ceil(a))