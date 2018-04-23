#!/usr/bin/env python

"""  statistic
#  ----
#  License: BSD
#  ----
#  0.1: init version - 2016.6 - by Nick Qian
"""


def statistic(bags):
    """example:
    Niu 1-9:  1:98598, 2:100122, 3:100394, 4:101250, 5:100785, 6:100239, 7:100176, 8:100327, 9:100417
    Niu 10:   97692             <NiuNiu>                     10%
    Niu 11-12: 22550, 22528     <DuiZi> <JinNiu>             2.25%
    Niu 13-15: 7455, 7515, 7620 <BaoZi> <ManNiu> <ShunZi>    0.75%
    rW_avg = (100000*(2 + 3 + 4+ 5 + 6 + 7 + 8 + 9 + 10) + 22540*(11 + 12) + 7500(13 + 14 +15) )/100,0000
                        (540,0000                      +    51,8420      +      31,5000 )/100,0000 = 6.23342%
    rL_avg = rW_avg
    """
    count_1, count_2, count_3, count_4, count_5  = 0,0,0,0,0
    count_6, count_7, count_8, count_9, count_0  = 0,0,0,0,0

    niuSum = []
    nius  = []

    BaoZi  = []
    ManNiu = []
    ShunZi = []
    DuiZi  = []
    JinNiu = []

    for threeWei in bags:
        if (threeWei[-4:] == '1.11') or (threeWei[-4:] == '2.22') or (threeWei[-4:] == '3.33'):
            if VERBOSE_B:
                print ("Info*: Baozi:", threeWei)
            BaoZi.append(threeWei)
        if (threeWei[-4:] == '1.00') or (threeWei[-4:] == '2.00') or (threeWei[-4:] == '3.00'):
            if VERBOSE_C:
                print ("Info*: ManNiu:", threeWei)
            ManNiu.append(threeWei)
        if (threeWei[-4:] == '1.23') or (threeWei[-4:] == '2.34') or (threeWei[-4:] == '3.45'):
            if VERBOSE_C:
                print ("Info*: ShunZi:", threeWei)
            ShunZi.append(ShunZi)
        if (threeWei[-4] == '0') and (threeWei[-2] == threeWei[-1] ):
            #print ("Info*: DuiZi:", threeWei)
            DuiZi.append(DuiZi)
        if (threeWei[-4] == '0') and (threeWei[-1] == '0'):
            #print ("Info*: JinNiu:", threeWei)
            JinNiu.append(JinNiu) 

    for threeInt in bags:
        niuSum.append( int(threeInt[-4]) + int(threeInt[-1]) + int(threeInt[-2]) )
    #print ("NiuSum is:", niuSum)
    for sumrlst in niuSum:
        sumrlstString = str(sumrlst)
        nius.append(int(sumrlstString[-1]))
    #print ("Niu are:", nius)

    for i in range(0, len(nius)):
        if nius[i] is 1:
            count_1 += 1
        if nius[i] is 2:
            count_2 += 1
        if nius[i] is 3:
            count_3 += 1
        if nius[i] is 4:
            count_4 += 1
        if nius[i] is 5:
            count_5 += 1
        if nius[i] is 6:
            count_6 += 1
        if nius[i] is 7:
            count_7 += 1
        if nius[i] is 8:
            count_8 += 1
        if nius[i] is 9:
            count_9 += 1
        if nius[i] is 0:
            count_0 += 1
    print ("Info: Freq Sum [0->9]:", count_0, count_1, count_2, count_3, count_4,
               count_5, count_6, count_7, count_8, count_9)
    print ("Info: Freq <BaoZi> <ManNiu> <ShunZi> <DuiZi> <JinNiu>:", len(BaoZi), len(ManNiu), len(ShunZi), len(DuiZi), len(JinNiu) )


def statistic_r(bags):   #rW & rL
    my_rW     = []
    my_rL     = []
    rW = 0
    rL = 0
    for n in range(0, (len(bags))/2):
        mybag  = bags[n*2]
        my_niu = computeOneBag(mybag)
        dealerbag  = bags[n*2+1]
        dealer_niu = computeOneBag(dealerbag)
        if VERBOSE_E:
            print("--my bag:%s, dealer bag:%s |my niu:%d, dealer niu:%d"%(mybag, dealerbag, my_niu, dealer_niu))
        if my_niu > dealer_niu:
            if VERBOSE_D:
                print("-->No.%d: I win :  %d" %(n, my_niu) )
            my_rW.append(my_niu)
            #dealer_rL.append[my_niu]
        elif my_niu < dealer_niu:
            if VERBOSE_D:
                print("-->No.%d: I lost: %d, " %(n, (0-dealer_niu)) )
            my_rL.append(0-dealer_niu)

    rW = (float(sum(my_rW))) / len(my_rW)
    rL = (float(sum(my_rL))) / len(my_rL)
    if VERBOSE_D:
        print ("Info: statistic_r: my_rW is:", my_rW, "my_rL is:", my_rL)
    print ("->statistic_r: rW is:",rW, "rL is:",rL)




