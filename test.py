#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyUtils import boby, mkOdt

def test(dec):
	print('-'*50)
	print('Testing '+str(dec))
	hexval = boby.decToHex(dec)
	print('decToBin : ', boby.decToBin(dec))
	print('decToHex : ', hexval)
	print('hexToBibi : ', boby.hexToBibi( hexval ))
	print('hexToAscii : ', boby.hexToAscii( hexval))
	

tests = [ 
	71, 16041922, 
	12, 25, 100, 254, 258, 352, 108, 
	0,1,2,3,15,16,17,18,
	32, 48, 64, 80, 96, 112, 128, 256,512,1024, 2048, 3072, 4096, 
	29061972, 19720629, 629, 
	30071973, 
	19220416, 416, 1604, 
	16,256,4096,65536, 
	15,255,4095,65535, 
	20240218, 1498, 
]
	
# test conv
for t in tests: 
	test(t)

# Tst OO
table = [['Décimale', '', 'BIBI', '', 'Notation']]
for i in tests:
	h = boby.decToHex(i) 
	s = boby.hexToBibi( h )
	row = [ i, '\n:\n', s, ' => ']
	for c in h: 
		row.append(  boby.ROOTPATH+'/img/'+str(c)+'.png' )

	table.append(row)
	
mkOdt.mkTab(table, 'tests')



