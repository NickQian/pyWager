#!/usr/bin/env python

"""  to plot result
#  ----
#  License: BSD
#  ----
#  0.1: init version - 2016.6 - by Nick Qian
"""

import string
import matplotlib.pyplot as plt
#import numpy as np



def plot(day, money):  # list, list

    plt.plot(day, money)
    plt.xlabel("Day")
    plt.ylabel("Money")

    plt.title('your money')
    #plt.legend()

    plt.show()





if __name__ == '__main__':

    x = [x for x in range(1, 50)]
    y = range(1, 50)

    plot(x, y)
