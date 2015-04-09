# -*- coding: utf-8 -*-

import thinkstats as ts
import sys

def Pumpkin(weights):
	mean , variance = ts.MeanVar(weights)
	print "mean",mean
	print "variance",variance
	print "standard deviation",variance**0.5

if __name__ == '__main__':
	weights = [0.5,1.5,1.5,96.0]
	Pumpkin(weights)
 