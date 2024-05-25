#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from typing import List

ROOTPATH = os.path.join( os.path.dirname(os.path.abspath(__file__)), '..')  

	
# Construction des phonemes BIBI
consonnes = ['h', 'b', 'c', 'd']
voyelles = ['o', 'a', 'e', 'i']
bibiPhonetic = []
for c in consonnes:
	for v in voyelles: 
		bibiPhonetic.append(c.upper()+v.upper())

# Equivalent ascii de la notation 71, le vecteur gauche->droite correspond au 1er bit
asciiArrows = { 0: u'\u25CB', 1: u'\u2191', 2: u'\u2190', 4: u'\u2193', 8: u'\u2192'  }
notationAscii = [
	asciiArrows[0], 
	asciiArrows[1], 
	asciiArrows[2], 
	asciiArrows[2] + asciiArrows[1], 
	asciiArrows[4], 
	asciiArrows[4] + asciiArrows[1], 
	asciiArrows[4] + asciiArrows[2], 
	asciiArrows[4] + asciiArrows[2] + asciiArrows[1], 
	asciiArrows[8], 
	asciiArrows[8] + asciiArrows[1], 
	asciiArrows[8] + asciiArrows[2], 
	asciiArrows[8] + asciiArrows[2] + asciiArrows[1],
	asciiArrows[8] + asciiArrows[4], 
	asciiArrows[8] + asciiArrows[4] + asciiArrows[1], 
	asciiArrows[8] + asciiArrows[4] + asciiArrows[2], 
	asciiArrows[8] + asciiArrows[4] + asciiArrows[2] + asciiArrows[1] 
]


# 
def getMaxDiv ( base: int, decNumber: int ) -> List[int] : 
	'''
	Retourne le plus grand diviseur de decNumber pour la base , et l'exposant.
	'''
	maxDiv= 1
	exp = 0
	while( maxDiv*base <= decNumber ):
		maxDiv = maxDiv * base
		exp += 1	
	return [maxDiv, exp]
	
# Retourne un tableau des valeurs
def decToBase( base: int, decNumber: int ) -> List[int]:
	hexVals = []
	divExp = getMaxDiv(base, decNumber)
	maxDiv = originalMaxDiv = divExp[0]
	exp = divExp[1]
	if 2 == base : lenModulo = 4
	elif 16 == base : lenModulo = 2
	divRes = decNumber
	#print("divExp", divExp)
	while( divRes/maxDiv > 0 ): 
		hVal = int(divRes/maxDiv);
		divRes = divRes - ( hVal*maxDiv );
		maxDiv = maxDiv/base;
		hexVals.append( hVal )
		#print(">>>", hVal, divRes, maxDiv, hexVals)
			
	for ie in range( len(hexVals)-1, exp):
		hexVals.append( 0 )
		#print("+++", 0, hexVals)

	while len(hexVals)%lenModulo > 0:
		hexVals = [0] + hexVals; 
		#print("---", 0, hexVals)
	
	return hexVals; #[::-1]; 

def decToHex( dec: int ) -> List[int]: 
	return decToBase(16, dec)
	
def decToBin( dec: int ) -> List[int]: 
	return decToBase(2, dec)


# Conversions
def hexToBibi ( hexNumber: List[int] ) -> str:
	phonetic = ''
	for h in hexNumber:
		phonetic += bibiPhonetic[h]
	return phonetic

def decToBibi(decNum: int):
	return hexToBibi(decToHex( decNum ))
	
# Un symbole pouvant contenir jusqu'à 4 caractères, on sépare par un point.
def hexToAscii ( hexNumber: List[int] ) -> str:
	s = ''
	n=0
	for h in hexNumber:
		s += notationAscii[h]
		if n < len(hexNumber)-1:
			s += '.'
		n += 1
	return s

def decToStr(dec: int) -> str : 
	bina = decToBin(dec) 
	strBin = ''
	for i in bina:
		#strBin = str(i)+strBin
		strBin += str(i)
	'''for i in range(4-len(strBin)):
		strBin = '0'+strBin'''
	return strBin #[-4:]

def decToClockStr(dec: int, forOds: bool = False) -> str :
	firstL = ''
	secondL = ''
	thirdL = ''
	hexVal = decToHex(dec)
	i=0
	middleSpace = '   '
	lastSpace = ' '
	if forOds: 
		lastSpace = ''
		middleSpace += ' '
	for h in hexVal:
		s = decToStr(h)
		if h > 0 :
			#print(">>>", h, s, hexVal)
			firstL += s[0] + middleSpace + s[3]
			secondL += asciiArrows[1] + middleSpace + asciiArrows[4]
			thirdL += s[1]+ lastSpace + asciiArrows[2] + lastSpace +s[2]
			if i < len(hexVal)-1 : 
				firstL += ' | '
				secondL += ' | '
				thirdL += ' | '
		i+=1
	return firstL+'\n'+secondL+'\n'+thirdL

def decToCounterClockStr(dec: int, forOds: bool = False) -> str :
	firstL = ''
	secondL = ''
	thirdL = ''
	hexVal = decToHex(dec)
	i=0
	middleSpace = '   '
	lastSpace = ' '
	if forOds: 
		lastSpace = ''
		middleSpace += ' '
	for h in hexVal:
		s = decToStr(h)
		firstL += s[0] + middleSpace + s[3]
		secondL += asciiArrows[1] + middleSpace + asciiArrows[4]
		thirdL += s[1]+ lastSpace + asciiArrows[2] + lastSpace +s[2]
		if i < len(hexVal)-1: 
			firstL += ' | '
			secondL += ' | '
			thirdL += ' | '
		i+=1
	return firstL+'\n'+secondL+'\n'+thirdL
	


if __name__ == '__main__':
	if len(sys.argv) > 1 : dec = int(sys.argv[1])
	else : dec = 71
	print("Dec :", dec)
	print("Bin :", decToBin(dec))
	print("D2S :", decToStr(dec))
	print("Clock")
	print(decToClockStr(dec))
	print("Hex :", decToHex(dec))
	print("Bibi:", decToBibi(dec))
	#print(decToCounterClockStr(dec))
	#print("Bin :", decToBin(dec))
	#print("Hex :", decToHex(dec))
	

