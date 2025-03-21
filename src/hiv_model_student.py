import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 1, 11)

A = 100          # 一个初始病毒载量，例如100 (任意单位)
alpha = 2.0      # 假设 α = 2.0/day
B = 0            # 暂时设为零
beta = 5.0       # 具有更大衰减速率，暂时不起作用，因为B=0

viral_load = A * np.exp(-alpha * time) + B * np.exp(-beta * time)

plt.plot(time, viral_load, label='Initial Model (B=0)')
plt.xlabel('Time (days)')
plt.ylabel('HIV Viral Load (arbitrary units)')
plt.title('HIV Viral load vs. Time (Initial Exploration)')
plt.legend()
plt.grid(True)
plt.show()

def load_hiv_data(filepath):
    data = np.loadtxt(filepath, delimiter=",")
    time_data = data[:, 0]  # 第一列是时间
    viral_data = data[:, 1]  # 第二列是病毒载量数据
    return time_data, viral_data

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        # TODO: 初始化模型参数
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta

    def viral_load(self, time):
        # TODO: 计算病毒载量
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)

    def plot_model(self, time，label="Model"):
        # TODO: 绘制模型曲线
        vl = self.viral_load(time)
        plt.plot(time, vl, '-', label=label)

def load_hiv_data(filepath):
    # TODO: 加载HIV数据
    try:
        data = np.loadtxt(filepath, delimiter=',', skiprows=1)  # 假设第一行是标题
        return data[:, 0], data[:, 1]  # 返回天数和病毒浓度
    except Exception as e:
        print(f"Error loading data: {e}")
    return np.array([]), np.array([])

def main():
    # TODO: 主函数，用于测试模型
    time_data, viral_data = load_hiv_data('HIVseries.csv')

    plt.plot(time_data, viral_data, 'ro', label='Experimental Data') # 'ro' 为红色圆点
    plt.xlabel('Time (days)')
    plt.ylabel('HIV Viral Load (arbitrary units)')
    plt.title('HIV Viral Load Data')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
