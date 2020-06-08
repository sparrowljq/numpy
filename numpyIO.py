import numpy as np
# numpy可以读写磁盘上的二进制文件或二进制数据NumPy 为 ndarray 对象引入了一个简单的文件格式：npy。
# npy 文件用于存储重建 ndarray 所需的数据、图形、dtype 和其他信息。
# 常用的 IO 函数有：
# load() 和 save() 函数是读写文件数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npy 的文件中。
# savze() 函数用于将多个数组写入文件，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npz 的文件中。
# loadtxt() 和 savetxt() 函数处理正常的文本文件(.txt 等)

arr = np.array([1, 2, 3, 4, 5])
np.save('E:\oufile',arr)

b = np.load(r'E:\oufile.npy')
# 输出结果为[1 2 3 4 5]
# print(b)
# numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez("E:\oufile1", a, b,sin_array = c)
r = np.load(r"E:\oufile1.npz")
# 输出结果为['sin_array', 'arr_0', 'arr_1']
# print(r.files)
# print(r["sin_array"])
# 输出结果为
# [[1 2 3]
#  [4 5 6]]
# print(r["arr_0"])
# 输出结果为[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
# print(r["arr_1"])

# savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。
a = np.array([1, 2, 3, 4, 5])
np.savetxt("out.txt", a)
b = np.loadtxt("out.txt")
# 输出结果为[1. 2. 3. 4. 5.]
print(b)
