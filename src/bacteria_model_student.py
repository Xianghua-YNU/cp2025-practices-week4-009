import numpy as np
import matplotlib.pyplot as plt

def W(t, A, tau):
    return A * (np.exp(-t/tau) - 1 + t/tau) #定义W(t)函数

t = np.linspace(0, 2, 500)      #定义时间范围，生成从0到2的500个等间距点

# （a）计算当A = 1，tau = 1的 W(t)
W_t = W(t, A=1, tau=1) 

plt.plot(t, W_t, label='W(t) with A=1, τ=1')# 绘制曲线
plt.xlabel('t')#坐标轴
plt.ylabel('W(t)')
plt.title('W(t) vs t')#图像标题
plt.legend()#显示图例
plt.grid(True)#添加网格线
plt.show()
                
# （b）使用不同的 τ 和 A 值绘制多条曲线
A_values = [1, 2, 3]
tau_values = [0.5, 1, 1.5]#定义参数组合
plt.figure(figsize=(10, 6))#设置图形大小

for A in A_values:
    for tau in tau_values:
        W_t = W(t, A, tau)
        plt.plot(t, W_t, label=f'A={A}, τ={tau}')
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('W(t) vs t with different A and τ')
plt.legend()#显示图例
plt.grid(True)
plt.show()

# (c)更改线条颜色和样式
linestyles = ['-', '--', '-.', ':']#定义不同的线条样式和颜色
colors = ['b', 'g', 'r', 'c']

# 绘制多条曲线
plt.figure(figsize=(10, 6))
for i, A in enumerate(A_values):#用于获取索引，以便为每条曲线分配不同的颜色和样式
    for j, tau in enumerate(tau_values):
        W_t = W(t, A, tau)
    plt.plot(t, W_t, linestyle=linestyles[i], color=colors[i], label=f'A={A}, τ={tau}')

plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('W(t) vs t with different A and τ')
plt.legend()#显示图例
plt.grid(True)
plt.show()

#（d）添加图例帮助潜在读者区分曲线,探索可用的其他图选项
plt.figure(figsize=(10, 6))
for i, A in enumerate(A_values):
    for j, tau in enumerate(tau_values):
        W_t = W(t, A, tau)
        plt.plot(t, W_t, color=colors[i], linestyle=linestyles[j], linewidth=2, label=f'A={A}, τ={tau}')#linewidth=2 设置线条宽度

plt.xlabel('t', fontsize=14)#设置字体大小
plt.ylabel('W(t)', fontsize=14)
plt.title('W(t) with different A and τ values', fontsize=16)
plt.legend(fontsize=12, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)#grid 的 linestyle 和 alpha 参数用于设置网格线的样式和透明度
plt.tight_layout()#自动调整子图参数，以避免重叠
plt.show()


import numpy as np
import matplotlib.pyplot as plt

data_A = np.loadtxt('g149novickA.txt', delimiter=',')# 加载数据
data_B = np.loadtxt('g149novickB.txt', delimiter=',')

time_A, value_A = data_A[:, 0], data_A[:, 1]# 提取时间和数据
time_B, value_B = data_B[:, 0], data_B[:, 1]

def V(t, A, tau):
    return A * (1 - np.exp(-t / tau))# 定义函数

plt.figure(figsize=(12, 6))# 绘制实验数据点

# 绘制g149novickA的数据
plt.subplot(1, 2, 1)#在一个图形窗口中同时显示两个实验数据集的图表
plt.scatter(time_A, value_A, label='Experimental Data A', color='blue', marker='o')#绘制实验数据的散点图
plt.xlabel('Time (hours)')
plt.ylabel('V(t)')
plt.title('Experimental Data A')
plt.legend()#显示图例

# 绘制g149novickB的数据
plt.subplot(1, 2, 2)#在一个图形窗口中同时显示两个实验数据集的图表
plt.scatter(time_B, value_B, label='Experimental Data B', color='red', marker='x')
plt.xlabel('Time (hours)')
plt.ylabel('V(t)')
plt.title('Experimental Data B')
plt.legend()#显示图例

plt.tight_layout()
plt.show()

# (a)尝试拟合曲线
A_guess = 1.0# 选择一些合理的初始值
tau_guess = 1.0

t_fit = np.linspace(0, max(time_A), 100)# 生成拟合曲线
V_fit = V(t_fit, A_guess, tau_guess)

plt.figure(figsize=(6, 6))# 绘制拟合曲线
plt.scatter(time_A, value_A, label='Experimental Data A', color='blue', marker='o')#散点图
plt.plot(t_fit, V_fit, label=f'Fit: A={A_guess}, τ={tau_guess}', color='green')
plt.xlabel('Time (hours)')
plt.ylabel('V(t)')
plt.title('Fitting Experimental Data A')
plt.legend()
plt.show()

# （b）对于g149novickB，丢弃时间大于10小时的数据
filtered_time_B = time_B[time_B <= 10]
filtered_value_B = value_B[time_B <= 10]

plt.figure(figsize=(6, 6))# 重新绘制g149novickB的数据
plt.scatter(filtered_time_B, filtered_value_B, label='Filtered Experimental Data B', color='red', marker='x')
plt.xlabel('Time (hours)')
plt.ylabel('V(t)')
plt.title('Filtered Experimental Data B (t <= 10 hours)')
plt.legend()
plt.show()

# 尝试拟合过滤后的数据
# 选择一些合理的初始值
A_guess_B = 0.1
tau_guess_B = 2.0

t_fit_B = np.linspace(0, max(filtered_time_B), 100)# 生成拟合曲线
V_fit_B = V(t_fit_B, A_guess_B, tau_guess_B)

plt.figure(figsize=(6, 6))# 绘制拟合曲线
plt.scatter(filtered_time_B, filtered_value_B, label='Filtered Experimental Data B', color='red', marker='x')
plt.plot(t_fit_B, V_fit_B, label=f'Fit: A={A_guess_B}, τ={tau_guess_B}', color='purple')
plt.xlabel('Time (hours)')
plt.ylabel('V(t)')
plt.title('Fitting Filtered Experimental Data B')
plt.legend()
plt.show()
