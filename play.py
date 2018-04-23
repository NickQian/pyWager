#!/usr/bin/env python

"""  play behavior
#  ----
#  License: BSD
#  ----
#  0.1: init version - 2016.6 - by Nick Qian
"""


def compare(number_pair):
    if number_pair[0] > number_pair[1]:
        return 1
    elif number_pair[0] < number_pair[1]:
        return -1


def gen_compareResult(times):
    list_pair = gen_randomList(times)
    list_result = []

    for i in range(0, times):
        number_pair = [list_pair[i], list_pair[i*2] ]
        list_result.append( compare(number_pair ) )

    return list_result


def play_once(list_result, bet, rate, moneyIn):
    WinLostOnce = iter[list_result]
    yield (moneyIn + (bet * rate)*WinLostOnce.next() )


def play_oneSection():
    moneyIn = 1
    bet = 1
    rate = 2
    gen_compareResult(1000000)
    while True:
        currentResult = play_once(list_result, bet, moneyIn)
        #if 






if __name__ == "__main__":

    play_oneSection()
