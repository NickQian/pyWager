#!/usr/bin/env python

"""  bet strategies
#  ----
#  License: BSD 
#  ----
#  0.1: init version - 2016.6 - by Nick Qian
"""

import random 

  

def bet_kelly(P, moneyInHand):  #P(win) = 1-Q
    Q = 1 - float(P)
    ODDS_MAX = 15
    rW_avg = 8.0688               #rW is:', 8.068785713972469, 'rL is:', -8.06888799114749 
    rW = 8.06888                  # ??? clean Win  rate
    rL = 8.06888                  # ??? clean loss rate
    #F = (P*B  - Q )  / B         # When rL = 1
    F  = (P*rW - Q*rL)/ rW
    
    #bet = (moneyInHand/ODDS_MAX) * F
    #bet = (moneyInHand/rW_avg) * F
    bet = (moneyInHand/rW_avg) * F
    """
    # 1:KILLED, YOU LOST 2: Killed offen. win little  3: bad   4: half result  6: 70% to best  7: near best
      8: 100W~110W/month   12:96W/month. still good  15: Still good. 1.2X times    20:95W/month. 1.5X times
      50:     #80-100: half result. many plays
    """
    
    if VERBOSE_B == True:
        print ("------------------F: %.2f, bet: %d, @%d-----------------" %(F, bet, moneyInHand))
    return int(bet)

def bet_gamblerFallacy(lost_sum, rate):
    bet_gf  = (lost_sum * 1.2)/rate
    return bet_gf

def gen_randomList(total_pair):
    list_pair = []
    for x in range(0,total_pair*2):
        list_pair.append(random.randint(0,9)) 
    return list_pair

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
        if 
                       
    
    

if __name__ == "__main__"
    play_oneSection()
 
 
    