#!/usr/bin/env python

"""  This is the top file to run
#  ----
#  License: BSD
#  ----
#  0.1.1 - move funcs to individual files
#  0.1   - init version - 2016.6 - by Nick Qian
"""


import sys
import plot as plot
from bet_strategy import bet_kelly
from cfg import *
from hongbao import faHongbao, qiang, qiang_fz, compute


PlayCNT = 0
IWin    = 0
ILost   = 0


def playOnce(myMoneyIn,  playersNum):
    global PlayCNT
    global IWin
    global ILost

    myBet = bet_kelly(P, myMoneyIn)
    bags = faHongbao(playersNum )

    if WITH_FZ:
        myNiuNiu, dealerNiuNiu = qiang_fz(bags, PlayCNT, playersNum)
    else:
        myNiuNiu, dealerNiuNiu = qiang(bags, playersNum)

    MyMoneyOut, Res = compute(myNiuNiu, dealerNiuNiu, myBet, myMoneyIn)

    PlayCNT += 1
    if (Res == "WIN"):
      IWin += 1
    if (Res == "LOST"):
      ILost += 1
    if VERBOSE_D:
        print ("Info: PlayCNT now is:", PlayCNT)
    return MyMoneyOut


def playOneDay(MyMoneyIn, playTimes, playersNum):
    MyMoneyOut = MyMoneyIn
    for i in range(0, playTimes):
        MyMoneyOut = playOnce(MyMoneyOut, playersNum)
        #print ("Info: Finish play once, MyMoneyOut is: ", MyMoneyOut)\
        if (i==playTimes-1):
            print ("U--> ENDED TODAY! @ %d ->" %PlayCNT )
        if (MyMoneyOut < 10 ):              #  <100 , get out
            print ("X--> KILLED TODAY! @ %d ->" %PlayCNT )
            break
        if MyMoneyOut > (MyMoneyIn * ENOUGH_OUT_LINE ):   #2.2-> 20% get out
            if VERBOSE_A is True:
                print ("*--> Enough,Out. @ %d ->" %PlayCNT )
            break

    #print ("=============> The END: MyMoneyOut is:", MyMoneyOut)
    return MyMoneyOut



def main():

    STATISTIC = False #True #False

    total = 100000
    MyMoneyIn = 20000              # every day bring 20000 in. 1W:bet = 260.  2W:bet=520
    #playersNum = int(raw_input("players Number:"))
    playersNum = 20
    playTimesOneDay  = 300 #300          #MAX Value

    if STATISTIC==True:
        playersNum = int(raw_input("playersNum:") )
        bags = faHongbao(playersNum)           # for statistic: 1. set playersNum to 5000; 2. faHongbao
        statistic(bags) 
        statistic_r(bags)
    else:
        Days = int(raw_input("total play days:") )
        #playOneDay(MyMoneyIn, playTimesOneDay, playersNum)
        for i in range(0, Days):
            total = total - MyMoneyIn
            #global PlayCNT
            PlayCNT = 0
            MyMoneyOut = playOneDay(MyMoneyIn, playTimesOneDay, playersNum)
            if VERBOSE:
                print("-------> Day %d: MyMoneyOut is: %d. Playtimes: %d" %(i, MyMoneyOut, PlayCNT))
            total = total + MyMoneyOut
            if (i != 0) and (i%365 == 0):
                print ("====>year %d: result is: %d" %(i/365, total) )
        #itertools.count(Days) 
        #plotXy

        print ("========== End total: %d. I Win %d times, lost %d times. P is:%.5f" %(total, IWin, ILost, (float(IWin))/(float(ILost+IWin)) )   )    





if __name__ == "__main__":

    main()
