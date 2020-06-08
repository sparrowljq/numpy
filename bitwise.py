import numpy as np
# Numpy位运算
# bitwise_and 对数组元素执行位与操作、bitwise_or 对数组元素执行位或操作、invert按位取反、
# left_shift向左移动二进制表示的位、right_shift向右移动二进制表示的位
# 也可以使用 "&"、 "~"、 "|" 和 "^" 等操作符进行计算
a, b = 13, 17
# 输出13,17的二进制0b1101 0b10001
print(bin(13), bin(17))
print('\n')
# 输出结果为1
# print(np.bitwise_and(13, 17))
# print(13 & 17)
# 说明13 的位反转，其中ndarray的dtype是uint8：
# 输出结果为13 的位反转，其中 ndarray 的 dtype 是 uint8：
print(np.invert(13))