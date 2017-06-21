#!/usr/bin/env python

""" play method: Weixin niuniu, generate hongbao
#  ----
#  License: BSD 
#  ----
#  0.1: init version - 2017.6 - by Nick Qian
"""

import random

def calRandomValue(total, num):     #min, max,

    total = float(total)
    num = int(num)          
    bags = []
    minBag = 0.01
    if(num < 1):
        return
    if num == 1:
        return

    
    i = 0
    while(i < num ):
        i += 1
        maxBag = total - minBag*(num - i)
        k = int( (num-i)/2 )
        if num-i <= 2:
            k = num - i
        if k != 0:
            maxBag = maxBag / k

        if maxBag < 0.03:
                maxBag = 0.03
        #print ("DDEEBBUUGG: int(maxBag*100) is:", int(maxBag*100) )

        money = random.randint(int(minBag*100), int(maxBag*100))
        money = float(money)/100
        total = total - money
        if i < num:
            if VERBOSE_E:
                print ("No.%d: %.2f; remain: %.2f" %(i, money, total) )
            bags.append("%.2f" %money)
        else:   # the last one. This is dummy process, for random num not for decimal
            if VERBOSE_E:
                print ("No. %d: %.2f; remain: %.2f" %(i, total, 0))
            bags.append("%.2f" %total)
    #print bags
    return bags
    
def faHongbao(playersNum):
    houzi = random.randint(1, 6) 
    redbagTotalAmount = playersNum * 2 + (float(houzi))/10   #
    
    if VERBOSE_C == True:
        print ("FaHongBao: redbagTotalAmount:", redbagTotalAmount, "playersNum: ", playersNum)
    bags = calRandomValue(redbagTotalAmount, playersNum)

    return bags

def qiang(bags, playersNum):
    myBagSN     = random.randint(0, playersNum-1) 
    dealerBagSN = random.randint(0, playersNum-1)
    while (myBagSN == dealerBagSN):
        dealerBagSN = random.randint(0, playersNum-1)
    if VERBOSE_D == True:
        print ("My SN:", myBagSN, "dealer SN:", dealerBagSN)
    myBag     = bags[myBagSN]
    dealerBag = bags[dealerBagSN]
    if VERBOSE_D == True:
        print ("My bag:", myBag, "dealerBag:", dealerBag )
    return myBag, dealerBag

def qiang_fz(bags, times, playersNum):  # with assistant
    
    dealerBagSN = random.randint(0, playersNum-1)
    dealerBag = bags[dealerBagSN]
    
    myBagSN     = random.randint(0, playersNum-1)
    #----- avoid same SN -----
    while (myBagSN == dealerBagSN):                   
        dealerBagSN = random.randint(0, playersNum-1)
        
    #---- avoid small bag -----
    myBag = bags[myBagSN]
    if (times%STRENGH_TUISUAN ==0) and (times !=0):                 # every 5 times fz 1
        while True:
            myBag = bags[myBagSN]
            rW = computeOneBag(myBag)
            if rW < 7:                    # 8 9 10
                myBagSN  = random.randint(0, playersNum-1)
                if VERBOSE_B:
                    print ('DEBUG_N::: request change bag once. rW now is:', rW)
            else:
                if VERBOSE_B:
                    print ('DEBUG_P::: request change bag success, or without N the org niu>7 | rW now is:', rW)
                break
    
    if VERBOSE_D == True:        
        print ("My SN:", myBagSN, "dealer SN:", dealerBagSN)
        print ("My bag:", myBag, "dealerBag:", dealerBag )
        
    return myBag, dealerBag

def compute(myBag, dealerBag, myBet, myMoneyIn):
    global IWin
    global ILost
    
    my_rW     = computeOneBag(myBag)
    if VERBOSE_C:
        print ("Info: my_rW is:", my_rW )
    dealer_rW = computeOneBag(dealerBag)
    if VERBOSE_C == True:
        print ("Info: dealer_rW is:", dealer_rW )
    if my_rW > dealer_rW:
        myMoneyOut = myMoneyIn + my_rW*myBet
        IWin += 1
    elif my_rW < dealer_rW:
        myMoneyOut = myMoneyIn - dealer_rW*myBet
        ILost += 1
    else:
        myMoneyOut = myMoneyIn          # ??? Speed of qiang ??

    if VERBOSE_B == True:
        print "$$$:", myMoneyOut-myMoneyIn, "| myMoneyOut is:", myMoneyOut
    return myMoneyOut


def computeOneBag(threeWei):        # string in
    rW = 0

    if (threeWei[-4:] == '1.11') or (threeWei[-4:] == '2.22') or (threeWei[-4:] == '3.33'):
        rW = 15         
        #print ("This Niu is Baozi", rW)
    elif (threeWei[-4:] == '1.00') or (threeWei[-4:] == '2.00') or (threeWei[-4:] == '3.00'):
        rW = 14
        #print ("This Niu is ManNiu", rW)
    elif (threeWei[-4:] == '1.23') or (threeWei[-4:] == '2.34') or (threeWei[-4:] == '3.45'):
        rW = 13        
        #print ("This Niu is ShunZi", rW)
    elif (threeWei[-4] == '0') and (threeWei[-2] == threeWei[-1] ):
        rW = 12         
        #print ("This Niu is DuiZi", rW)
    elif (threeWei[-4] == '0') and (threeWei[-1] == '0'):
        rW = 11         
        #print ("This Niu is JinNiu", rW)
    else:
        niuSum = int(threeWei[-4]) + int(threeWei[-1]) + int(threeWei[-2]) 
        niu = int(str(niuSum)[-1])
        if niu == 0:
            niu = 10
        #print ("This Niu is: ", niu)
        rW = niu
    
    return rW
    
