import numpy as np

# 建立一个一维数组 Ndarray 表示N维数组对象
a = np.array([1, 2, 3])
# print(a)
# 建立一个二维数组
a = np.array([[1, 2], [3, 4]])
# print(a)

# 指定最小维度
a = np.array([1, 2, 3, 4, 5], ndmin=2)
# 输出结果为[[1 2 3 4 5]]
# print(a)

# dtype参数 数组元素的数据类型，可选
# 创建的虚数 形式为a+0*j
a = np.array([(1, 2), (3, 4)], dtype=complex, copy=True)
# print(a)

#NumPy数据类型
# numpy.dtype(object, align, copy) object 要转换为的数据类型对象 align 如果为true，
# 填充字段使其类似于C的结构体 copy复制dype对象，如果为false，则是对内置数据类型对象的引用

dt =np.dtype(np.int32)
# int32
# print(dt)
# int8,int16,int32,int64 四种数据类型可以使用字符串‘i1’,'i2','i4','i8'代替
dt = np.dtype('i4')
# int32
# print(dt)

# 数据的字节顺序（小端法或大端法）
dt = np.dtype('<i4')
# 数据结果为int32
# print(dt)

# 创建结构化的数据类型
dt = np.dtype([('age', np.int8)])
# [('age', 'i1')]
# print(dt)

# 将数据类型应用于ndarray
a = np.array([1, 2, 3], dtype=dt)
# 输出结果为[(1,) (2,) (3,)]
# print(a)
# 类型字段名可以用于存取实际的age列
# [1 2 3]
# print(a['age'])
# 下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，
# 及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
# 输出结果为[(b'abc', 21, 50.) (b'xyz', 18, 75.)]
# print(a)
# numpy.arange(start, stop, step, dtype)
# NumPy数组的维数称为秩，比如一维数组的秩为1，二维数组的秩为2
a = np.arange(24)
# 返回数组的秩
# print(a.ndim)
# 重定义数组a的形状
b = a.reshape(2, 3, 4)
# 输出结果是3
# print(b.ndim)
# ndarray.shape表示数组的维度，返回一个元组。这个元组的长度就是维度的数目，
# 例如一个二维数组，其维度表示“行数”和“列数”
a = np.array([[1, 2, 3], [2, 3, 4]])
# 输出结果为(2, 3)
# print(a.shape)

# 调整数组大小
a = np.array([[1, 2, 3],[4, 5, 6]])
# 输出结果为
# [[1 2 3]
#  [4 5 6]]
#print(a)
a.shape = (3, 2)
# 输出结果
# [[1 2]
#  [3 4]
#  [5 6]]
# print(a)
a.reshape(3, 2)
# print(a)
# 返回每一个元素的大小

# 以字节的形式返回数组中每个元素的大小
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
# 输出结果为1
# print(x.itemsize)
# 返回对象的内存信息
# print(x.flags)
a = np.arange(24)
# 输出数组
# print(a)

# 创建数组
# 数组除了使用底层ndarray构造器来创建之外，还可以通过以下方式来创建
# numpy.empty 创建 一个指定形状（shape）、数据类型（dtype）且未初始化的数组
# numpy.empty(shape,dtype =float,order='C')
# order 有C和F两个选项，分别表示行优先和列优先
x = np.empty([3, 2], dtype=int)
# print(x)
# numpy.zeros 创建指定大小的数组，数组元素以0来填充
x = np.zeros([3, 2], dtype=float, order='C')
# 输出结果为
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]
# print(x)
# 设置自定义类型
dt = np.dtype([('age', 'i4'), ('name', 'S20')])
x = np.zeros([3, 2], dtype=dt, order='C')
# 输出结果为
# [[(0, b'') (0, b'')]
#  [(0, b'') (0, b'')]
#  [(0, b'') (0, b'')]]
# print(x)
# 给数组元素赋值
x[0][1]['age'] = 13
x[0][1]['name'] ='kobe'
# 输出结果为
# [[( 0, b'') (13, b'kobe')]
#  [( 0, b'') ( 0, b'')]
#  [( 0, b'') ( 0, b'')]]
# print(x)
# numpy.ones使用方法
x = np.ones([2, 2], dtype=int, order='C')
# 输出结果为
# [[1 1]
#  [1 1]]
# print(x)

# Numpy从数值范围创建数组
# numpy.arange(start, stop, step, dtype)
x = np.arange(1, 10, 2, int)
# 输出结果为[1 3 5 7 9]
# print(x)

# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# num表示样本的数量
x = np.linspace(1, 10, 10)
# print(x)
# 生成全为2的等差数列
x = np.linspace(2, 2, 10)
# 输出结果为[2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
# print(x)
# 不包含终止值
x = np.linspace(1, 11, 10, endpoint=False)
# 输出结果为[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# print(x)

x = np.linspace(1, 11, 10, endpoint=False,retstep=True)
# 输出结果为(array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
# print(x)

# numpy.logspace 函数用于创建一个于等比数列
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# base表示对数的底数
x = np.logspace(0, 9, 10, base=2)
# 输出结果为[  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]
print(x)