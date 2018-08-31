import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
def len_reg(dataset_0,dataset_1):
    sigma_x_sq = np.sum(dataset_0 ** 2)
    sigma_x = np.sum(dataset_0)
    sigma_y = np.sum(dataset_1)
    sigma_xy = np.sum(dataset_0 * dataset_0)
    lis = len(dataset_0)
    n = lis
    # print(sigma_x_sq,sigma_x,n,sigma_y)
    a = np.array([[sigma_x_sq, sigma_x], [sigma_x, n]])
    b = np.array([sigma_xy, sigma_y])
    sol = np.linalg.solve(a, b)
    print(sol)
    x = input("Enter the value of x to predict:")
    y = sol[0] * x + sol[1]
    print(y)
    x_val = np.linspace(0, 10, 100)
    y_val = np.array(map(lambda b: sol[0] * b + sol[1], x_val))
    plt.plot(x_val, y_val)
    plt.scatter(dataset_0, dataset_1)
    plt.xlabel("% of class")
    plt.ylabel("vote obtained")
    plt.show()

