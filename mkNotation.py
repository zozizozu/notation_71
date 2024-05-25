#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyUtils import boby, mkOdt


def mkRow(i):
	bina = boby.decToBin(i) 
	strBin = boby.decToStr(i)
	strBinSq = boby.decToClockStr(i, True)
	hexa = boby.decToHex(i) 
	bibi = boby.hexToBibi( hexa )
	return [ i, strBin, strBinSq, boby.ROOTPATH+'/img/'+str(i)+'.png', bibi ]
	
table = [ ['Décimal', 'Binaire', 'Représentation\nhoraire', 'Notation', 'BiBi'] ]
for i in range(16):
	row = mkRow(i)
	table.append(row)
	#print(row)

	
mkOdt.mkTab(table, 'Notation_71')
