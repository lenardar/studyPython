# 使用梯度下降法获得线性回归模型
import numpy as np
import random
import math

# 批量梯度下降GBD


def BGD(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5):
    m = X.shape[0]
    n = X.shape[1]
    omega = np.zeros((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量
    for i in range(num_iters):
        h = X @ omega

        g = 2*np.dot(X.T, (h-y))  # 计算梯度

        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        minus = alpha * g
        if np.linalg.norm(minus) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - minus
            break
        omega = omega - minus
    return omega


# 小批量梯度下降MBGD
def MBGD(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5, batch_size=1):
    m = X.shape[0]
    n = X.shape[1]
    omega = np.zeros((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量

    for i in range(num_iters):
        list_batch = random.sample(range(m), batch_size)
        X_batch = X[list_batch]
        y_batch = y[list_batch]

        h = X_batch @ omega
        g = 2*np.dot(X_batch.T, (h-y_batch))  # 计算梯度
        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        minus = alpha * g
        if np.linalg.norm(minus) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - minus
            break
        omega = omega - minus

    return omega


# MBGD动量法
def MBGD_Momentum(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5, batch_size=1, beta=0.9):
    m = X.shape[0]
    n = X.shape[1]
    omega = np.ones((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量
    v = np.zeros((n, 1))  # 初始化动量

    for i in range(num_iters):
        list_batch = random.sample(range(m), batch_size)
        X_batch = X[list_batch]
        y_batch = y[list_batch]

        h = X_batch @ omega
        g = 2*np.dot(X_batch.T, (h-y_batch))  # 计算梯度
        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        v = beta * v + alpha * g
        if np.linalg.norm(v) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - v
            break
        omega = omega - v

    return omega


# MGBD牛顿动量法
def MBGD_Nesterov(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5, batch_size=1, beta=0.9):
    m = X.shape[0]
    n = X.shape[1]
    omega = np.ones((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量
    v = np.zeros((n, 1))  # 初始化动量

    for i in range(num_iters):
        list_batch = random.sample(range(m), batch_size)
        X_batch = X[list_batch]
        y_batch = y[list_batch]
        
        omega_ahead = omega+beta*v

        h = X_batch @ omega_ahead
        g = 2*np.dot(X_batch.T, (h-y_batch))  # 计算梯度
        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        v = beta * v + alpha * g
        if np.linalg.norm(v) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - v
            break
        omega = omega - v

    return omega


# AdaGrad
def AdaGrad(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5, batch_size=1,e=1e-5):
    # s为分母初始值
    # e防止分母为0，默认设置一个小正数
    m = X.shape[0]
    n = X.shape[1]
    omega = np.zeros((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量
    list_g = np.zeros(num_iters)  # 存储历史梯度平方值
    s = 0  # 分母初始值

    for i in range(num_iters):
        list_batch = random.sample(range(m), batch_size)
        X_batch = X[list_batch]
        y_batch = y[list_batch]

        h = X_batch @ omega
        g = 2*np.dot(X_batch.T, (h-y_batch))  # 计算梯度
        s = s + np.linalg.norm(g)**2
        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        alpha_adj = alpha / np.sqrt(s+e)
        minus = alpha_adj * g
        if np.linalg.norm(minus) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - minus
            break
        omega = omega - minus

    return omega


# RMSProp
def RMSProp(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5, batch_size=1, e=1e-5, rho=0.1):
    # s为分母初始值
    # e防止分母为0，默认设置一个小正数
    m = X.shape[0]
    n = X.shape[1]
    omega = np.zeros((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量
    list_g = np.zeros(num_iters)  # 存储历史梯度平方值
    s = 0  # 分母初始值

    for i in range(num_iters):
        list_batch = random.sample(range(m), batch_size)
        X_batch = X[list_batch]
        y_batch = y[list_batch]

        h = X_batch @ omega
        g = 2*np.dot(X_batch.T, (h-y_batch))  # 计算梯度
        s = rho*s + (1-rho)*np.linalg.norm(g)**2
        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        alpha_adj = alpha / np.sqrt(s+e)
        minus = alpha_adj * g
        if np.linalg.norm(minus) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - minus
            break
        omega = omega - minus

    return omega


# Adam
def Adam(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5, batch_size=1, e=1e-5, rho_1=0.1, rho_2=0.1):
    # alpha为学习率
    # s为RMSProp分母初始值，e防止RMSProp分母为0
    # rho_1为动量参数
    # rho_2为RMSProp参数
    m = X.shape[0]
    n = X.shape[1]
    omega = np.zeros((n, 1))
    y = y.reshape(-1, 1)  # 将y转换为列向量
    v = np.zeros((n, 1))  # 定义初速度
    s = 0  # 分母初始值

    for i in range(num_iters):
        list_batch = random.sample(range(m), batch_size)
        X_batch = X[list_batch]
        y_batch = y[list_batch]

        h = X_batch @ omega
        g = 2*np.dot(X_batch.T, (h-y_batch))  # 计算梯度
        v = rho_1*v+(1-rho_1)*g
        s = rho_2*s + (1-rho_2)*np.linalg.norm(g)**2
        if np.linalg.norm(g) < epsilon:   # 当梯度小于阈值时停止迭代
            break
        V = v/(1-rho_1**(i+1))
        S = s/(1-rho_2**(i+1))
        minus = alpha*V/(np.sqrt(S)+e)
        if np.linalg.norm(minus) < epsilon:  # 当函数值稳定时停止迭代
            omega = omega - minus
            break
        omega = omega - minus

    return omega



# 牛顿法
def Newton(X, y, alpha=0.01, num_iters=1000, epsilon=1e-5):
    m, n = X.shape
    omega = np.zeros((n, 1))
    H = X.T @ X  # Hessian矩阵
    H_inv = np.linalg.inv(H)  # Hessian矩阵的逆
    y = y.reshape(-1, 1)  # 将y转换为列向量

    for i in range(num_iters):
        h = X @ omega  # 计算预测值
        grad = 2 * X.T @ (h - y)  # 计算梯度
        if np.linalg.norm(grad) < epsilon:
            break
        omega = omega - alpha * H_inv @ grad  # 牛顿法更新公式

    return omega


# 测试
if __name__ == '__main__':
    X = np.array([[200, 150, 1], [900, 200, 1], [120, 250, 1], [234, 300, 1], [
                 500, 350, 1], [400, 400, 1], [230, 600, 1]], dtype=float)
    x_max = np.amax(X[:, 0])
    x_min = np.amin(X[:, 0])
    X[:, 0] = (X[:, 0]-x_min)/(x_max - x_min)
    x_max = np.amax(X[:, 1])
    x_min = np.amin(X[:, 1])
    X[:, 1] = (X[:, 1]-x_min)/(x_max - x_min)
    print('X为：')
    print(X)

    y = np.array([6450, 7450, 8450, 9450, 11450, 15450, 18450])
    y = (y-6450)/(18540-6450)
    print('y为：')
    print(y)

    omega = Adam(X, y)
    print('omega为：')
    print(omega)
