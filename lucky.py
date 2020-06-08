from matplotlib import pyplot as plt
import numpy as np
# Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。
# 它也可以和图形工具包一起使用，如 PyQt 和 wxPython
# x = np.arange(1, 11)
# y = 2*x + 5
plt.title("matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
# 绘制函数图像
#plt.plot(x, y)
# plt.plot(x, y, "ob") # o表示圆点、b表示蓝色
# plt.show()

# x = np.arange(0,  3  * np.pi,  0.1)
# y = np.sin(x)
# y_cos = np.cos(x)
# plt.title("sine wave form")
# # 使用 matplotlib 来绘制点
# plt.subplot(2,  1,  1)
# plt.plot(x, y)
# plt.title('Sine')
# # 第二个数字表示图像要显示在第几个图片上
# plt.subplot(2,  1,  2)
# plt.plot(x, y_cos)
# plt.title('cosine')
# plt.show()
# 生成条形图
# x =  [5,8,10]
# y =  [12,16,6]
# x2 =  [6,9,11]
# y2 =  [6,15,7]
# plt.bar(x, y, align =  'center')
# plt.bar(x2, y2, color =  'g', align =  'center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

# 生成numpy.histogram() 函数是数据的频率分布的图形表示。
# 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a,bins =[0,20,40,60,80,100])
plt.title("histogram")
plt.show()