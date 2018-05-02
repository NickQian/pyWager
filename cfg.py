#!/usr/bin/env python

""" config file
#  ----
#  License: BSD
#  ----
#  0.1   - init version - 2018.4 - by Nick Qian
"""


STRENGH_TUISUAN =  3                          # Insert every x times
"""Config STRENGH_TUISUAN to config the P value
example: (10, P=0.529, F=0.06)  (8, P=0.54, F=0.08)   (7, P=0.547, F=0.09)  (6, P=0.55, F=0.10) 
         (5,  P=0.562, F=0.12)  (4, P=0.58, F=0.16)   (*3, P=0.606, F =0.21)
"""
P = 0.606                                     # according last config

ENOUGH_OUT_LINE       = 3.2                   #1.2-> 20% get out           Big: play many times. Song_Min mode
UNLIMITED_MONEY       = 1000000000000.0
RICH_GUY_MONEY        = 90000000.0
MIN_BET_LIMIT         = 300                   # according the "Venetian Macau"
PLAY_TIMES_DAY_LIMIT  = 300                   # 3 minutes once, play 15 hours one day

MyMoneyInEveryDay = 200000.0
playersNum        = 20

VERBOSE = True                                # False
VERBOSE_A = False                             # daily report
VERBOSE_B = False                             # bet info /win lost info/Fuzhu info
VERBOSE_C = False                             # FaHongBao prompt and my rW/dealer rW
VERBOSE_D = False                             # My SN and bag I get
VERBOSE_E = False                             # Red bag info



