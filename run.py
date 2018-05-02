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
from bet_strategy import bet_kelly, bet_average
from cfg import *
from hongbao import faHongbao, qiang, qiang_fz, compute


PlayCNT = 0
IWin    = 0
ILost   = 0


def playOnce(myMoneyIn,  playersNum, With_FuZhu, Bet_Strategy):
    global PlayCNT
    global IWin
    global ILost


    if(Bet_Strategy =="KELLY"):
        myBet = bet_kelly(P, myMoneyIn)
    elif(Bet_Strategy == "AVERAGE") :
        myBet = bet_average()

    if myBet < MIN_BET_LIMIT:
        print("@@@@@: Too little bet. The 'Venetian Macau' limits $300.@@@ ")
        return myMoneyIn

    bags = faHongbao(playersNum )

    if With_FuZhu:
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
        print ("Info: PlayCount now is:", PlayCNT)

    return MyMoneyOut



def playOneDay(MyMoneyIn, playTimes, playersNum, With_FuZhu, Bet_Strategy, Enough_Out):
    global PlayCNT

    MyMoneyOut = MyMoneyIn
    for i in range(0, playTimes):
        MyMoneyOut = playOnce(MyMoneyOut, playersNum, With_FuZhu, Bet_Strategy)
        if (i==playTimes-1):
            print ("-     ENDED TODAY  @ %d ->" %PlayCNT )
        if (MyMoneyOut < MIN_BET_LIMIT):                            # <100 , get out
            print ("x     KILLED TODAY! @ %d ->" %PlayCNT )
            break
        if MyMoneyOut > (MyMoneyIn * Enough_Out ):   #2.2-> 20% get out
            print ("*     Enough Today. @ %d ->" %PlayCNT )
            break

    return MyMoneyOut




def gamble_method_sel():

    ######## P select ########
    P_method = raw_input("""Please select P method:
1: P = 0.5;
2: P > 0.5
:""")

    if (P_method == "1"):
        With_FuZhu = False
    elif (P_method == "2"):
        With_FuZhu = True
    else:
        print("Error Input!")
        exit_run()

    ########### strategy select ################
    Gambler_method = raw_input("""please select gambler method
a) ...
b) ...
c) ...
d) ...
:""")

    if Gambler_method   == "a":
        Enough_Out  = 1.2
        Total_Money = UNLIMITED_MONEY
    elif Gambler_method == "b":
        Enough_Out  = 1.2
        Total_Money = RICH_GUY_MONEY
    elif Gambler_method == "c":
        print("Not implemented. ")
        exit_run()
    elif Gambler_method == "d":
        print("Not implemented. ")
        exit_run()
    else:
        print("Error Input!")
        exit_run()


    ######## bet method select ########
    bet_method = raw_input("""Please select bet method:
1: average bet method;
2: kelly bet method
:""")

    if (bet_method == "1"):
        Bet_Strategy = "AVERAGE"
    elif (bet_method == "2"):
        Bet_Strategy = "KELLY"
    else:
        print("Error Input!")
        exit_run()


    ############  days #################
    Days = int(raw_input("total play days:") )
    if (Days <= 0):
        print("Error Input!")
        exit_run()

    return With_FuZhu, Enough_Out, Total_Money, Bet_Strategy, Days





def run_P_statistic():
    playersNum = int(raw_input("playersNum:") )
    bags = faHongbao(playersNum)           # for statistic: 1. set playersNum to 5000; 2. faHongbao
    statistic(bags)
    statistic_r(bags)



def main():

    STATISTIC = False      #True #False
    global PlayCNT


    if STATISTIC==True:
        run_P_statistic()
    else:
        With_FuZhu, Enough_Out, total, Bet_Strategy, Days = gamble_method_sel()

        for i in range(0, Days):
            total = total - MyMoneyInEveryDay
            PlayCNT = 0                        # every day reset palyCNT.
            MyMoneyOut = playOneDay(MyMoneyInEveryDay, PLAY_TIMES_DAY_LIMIT, playersNum, With_FuZhu, Bet_Strategy, Enough_Out)
            if VERBOSE:
                print("----> Day %d: MyMoneyOut is: %d. Playtimes: %d" %(i, MyMoneyOut, PlayCNT))
            total = total + MyMoneyOut
            if (i != 0) and (i%365 == 0):
                print ("====>year %d: result is: %d" %(i/365, total) )

        #itertools.count(Days)
        #plotXy

        print ("========== End total: %d. I Win %d times, lost %d times. P is:%.5f" %(total, IWin, ILost, (float(IWin))/(float(ILost+IWin)) )   )    




def exit_run():
    sys.exit()






if __name__ == "__main__":

    main()
