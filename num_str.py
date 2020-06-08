# 字符串函数
import numpy as np
# 连接两个字符串
# 输出结果['helloworld']
# print(np.char.add(['hello'], ['world']))
# 输出结果为['helloabc' 'worldxyz']
# print(np.char.add(['hello', 'world'], ['abc', 'xyz']))

# numpy.char.multiply() 函数执行多重连接
# 输出结果worldworldworld
# print(np.char.multiply('world', 3))
# numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充
# 输出结果为*******world********
# print(np.char.center('world', 20, fillchar='*'))
# numpy.char.capitalize() 函数将字符串的第一个字母转换为大写
# 输出结果为Helloworld
# print(np.char.capitalize('helloworld'))
# numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写
# 输出结果为Hello World
# print(np.char.title('hello world'))
# numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower
# 输出结果为['runoob' 'google']
# print(np.char.lower(['RUNOOB', 'GOOGLE']))
# numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper

# numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格
# 输出结果为['i', 'like', 'runoob']
# print(np.char.split('i like runoob'))
# 输出结果为['www', 'baidu', 'com']
# print(np.char.split('www.baidu.com', sep='.'))
# numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组 \n，\r，\r\n 都可用作换行符。
# 输出结果为['i', 'like runoob?']
# print(np.char.splitlines('i\nlike runoob?'))
# 输出结果['i', 'like runoob?']
# print(np.char.splitlines('i\rlike runoob?'))

# numpy.char.strip()函数用于移除开头或结尾处的特定字符
# 输出结果为
# print(np.char.strip('ashok arunooba', 'a'))
# 输出结果为['dimin' 'head' 'pple']
# print(np.char.strip(['adimin', 'ahead', 'apple'], 'a'))
# numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
# 输出结果为r:u:n:o:o:b
# print(np.char.join(':', 'runoob'))
# 指定多个字符分割元素
# 输出结果为['h:e:l:l:o' 'w-o-r-l-d']
# print(np.char.join([':', '-'], ['hello', 'world']))

# numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串
# 输出结果为i like runccb
# print(np.char.replace('i like runoob', 'oo', 'cc'))

# numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数
# 输出结果为b'\x99\xa4\x95\x96\x96\x82'
# print(np.char.encode('runoob', 'cp500'))

# a = b'\x99\xa4\x95\x96\x96\x82'
# 输出结果为runoob
# print(np.char.decode(a, 'cp500'))