import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import scipy.stats as stats
import math


def f(row):
    if row['Gender'] == 'M':
        return 0
    return 1

def clustering():
    print("Clustering")
    df = pd.read_csv("ebenezer.csv")
    x_axis = np.arange(-10, 10, 0.001)
    plt.plot(x_axis, norm.pdf(df['Time'], 0, 2))
    plt.show()

    mean = math.mean()
    print("Mean: " + mean)
    #df['Color'] = df.apply(f, axis=1)

    #male = data.select(data['Gender'] == 'M')

    return

    male = df.loc[df['Gender'] == 'M']
    female = df.loc[df['Gender'] == 'F']

    plt.scatter(male['Time'], male['Age'], c='blue', alpha=0.2, s=120, edgecolors='none', label='Male')
    plt.scatter(female['Time'], female['Age'], c='red', alpha=0.2, s=120, edgecolors='none', label='Female')
    plt.scatter(30.19, 36, s=120, marker='d', label='Schalk', edgecolors='black')
    plt.scatter(31.28, 33, s=120, marker='d', label='Tiaan', edgecolors='black')
    plt.scatter(38.24, 49, s=120, marker='d', label='Neal', edgecolors='black')
    plt.scatter(39.13, 40, s=120, marker='d', label='JP', edgecolors='black')
    plt.scatter(47.16, 42, s=120, marker='d', label='Johan', edgecolors='black')
    plt.ylabel('Age (Years)')
    plt.xlabel('Time (s)')
    plt.legend();

    plt.show()




def main():
    print("Hello world")

    #print(reverse(123))
    #print(reverse_bits("00000010100101000001111010011100"))
    clustering()


# @param n, an integer
# @return an integer
def reverse_bits(n):
    # TODO
    return n


def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    negative_number = False
    if x < 0:
        x *= -1
        negative_number = True

    r_string = ""
    x_string = str(x)
    for i in x_string:
        r_string = i + r_string

    x = int(r_string)

    # Catch for return of 32-bit signed integers missing for edge cases...
    if x < -(2 ** 31) or x > (2 ** 31) - 1:
        return 0

    if negative_number:
        return -1*x
    return x


if __name__ == "__main__":
    main()

