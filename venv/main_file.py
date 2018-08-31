# file header:ward_no,rich_class,higher_class,
import linear_regression as lr
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def read_file(file_name):
    file_name+=".csv"
    data = pd.read_csv(file_name, header=None)
    print(data)
    print("Select any of the following option:")
    print(
        "1.Rich Class Plot\n2.Higher Class Plot\n3.Upper middle class Plot\n4.Lower middle class Plot\n5.Poor class Plot")
    option = input("Enter your option:")
    print(option)
    if (option == 1):
        z = data[option]
        y = data[6]
        lr.len_reg(z,y)
        x = data[0]
    elif (option == 2):
        z = data[option]
        y = data[6]
        x = data[0]
        lr.len_reg(z,y)

    elif (option == 3):
        z = data[option]
        y = data[6]
        x = data[0]
        lr.len_reg(z,y)

    elif (option == 4):
        z = data[option]
        y = data[6]
        x = data[0]
        lr.len_reg(z,y)

    elif (option == 5):
        z = data[option]
        y = data[6]
        x = data[0]
        lr.len_reg(z,y)

    else:
        print("Wrong Entry")
    lis=[x,y,z]
    return lis
def plot_3d(file_name):
    lis=read_file(file_name)
    x=lis[0]
    y=lis[1]
    z=lis[2]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c="r", marker="o")
    ax.set_xlabel("ward no")
    ax.set_ylabel("votes")
    ax.set_zlabel("% of class")
    plt.show()

if __name__=="__main__":
    plot_3d("test")