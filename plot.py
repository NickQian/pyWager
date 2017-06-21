#!/usr/bin/env python

"""  to plot result
#  ----
#  License: BSD 
#  ----
#  0.1: init version - 2016.6 - by Nick Qian
"""

import string
import matplotlib.pyplot as plt  
import numpy as np

def plot(day, money):  # number, number
    x_day = day
    #x_days = [x for x in range(days)]
    y_money = money
    

def plotXy(x, y):
    plt.plot(x, y, 'b')
    plt.xlabel("Day")
    plt.ylabel("Money")
    plt.show()
 
if __name__ == '__main__':
    times = 6
    Days = [x for x in range(0, times)]         #(itertools.count(Days)).next()
    print Days
    money = [1,4,6,3,8,9]
    plotXy(Days, money)
    
    

'''
    file = open(E:machine_learningdatasetshousing_datahousing_data_ages.txt, 'r')
    linesList = file.readlines()
#     print(linesList)
    linesList = [line.strip().split(,) for line in linesList]
    file.close()    
    print(linesList:)
    print(linesList)
#     years = [string.atof(x[0]) for x in linesList]
    years = [x[0] for x in linesList]
    print(years)
    price = [x[1] for x in linesList]
    print(price)
    plt.plot(years, price, 'b*')#,label=$cos(x^2)$)
    plt.plot(years, price, 'r')
    plt.xlabel(years(+2000))
    plt.ylabel(housing average price(*2000 yuan))
    plt.ylim(0, 15)
    plt.title('line_regression & gradient decrease')
    plt.legend()
    plt.show()
'''
