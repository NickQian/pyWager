#!/usr/bin/env python

""" play method: coin tossing
# ---
# License: BSD
# ---
# 0.1: init version - 2019.12 - by Nick Qian
"""

import random
from cfg import *


def GenRedGreen(len):
	tradres = []
	i = 0;
	while (i < len):
		i += 1
		float0_1 = random.random()     # 0 ~ 1
		tradres.append(float("%.2f" %(float0_1 - 0.5)) )

	j_pos, j_neg, j_zero = statsPosNeg(tradres)
	print("tradres, j_pos, j_neg, j_zero:" , tradres, j_pos, j_neg, j_zero)

	return tradres


def statsPosNeg(theList):
	j_pos =0; j_neg =0; j_zero =0;
	for e in theList:
		if e > 0.00:
			j_pos  += 1
		if e < 0.00:
			j_neg  += 1
		if e ==0.00:
			j_zero += 1
	return j_pos, j_neg, j_zero


def betOn_N(tradres, N):
	ColPos_, ColNextE = travIt(tradres, N)
	return ColPos_, ColNextE



def travIt(tradres, num):
	ColNextE = []
	for i, val in enumerate(tradres):
		FlgPos = True
		for k in range(num):
			if i+k < len(tradres) and tradres[i+k] <0.0:
				FlgPos = False
		if FlgPos == True:
			ColPos_ = tradres[i:i+num+1]
			print("###:ColPos_:", ColPos_)
			if len(ColPos_) == num+1:   # to avoid last numers
				ColNextE.append(ColPos_[num])
	print("--->", ColNextE)
	return ColPos_, ColNextE





if __name__ == "__main__":
	tradres = GenRedGreen(20000)
	ColPos_, ColNextE = betOn_N(tradres, 5)
	j_pos, j_neg, j_zero = statsPosNeg(ColNextE)
	print("===>j_pos, j_neg, j_zero:", j_pos, j_neg, j_zero)
