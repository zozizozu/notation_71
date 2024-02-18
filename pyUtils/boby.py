#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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
	asciiArrows[8] + asciiArrows[4] +asciiArrows[1], 
	asciiArrows[8] + asciiArrows[4] + asciiArrows[2], 
	asciiArrows[8] + asciiArrows[4] + asciiArrows[2] + asciiArrows[1] 
]


# Retourne le plus grand diviseur pour la base et l'exposant
def getMaxDiv ( base, decNumber ): 
	maxDiv= 1
	exp = 0
	while( maxDiv*base <= decNumber ):
		maxDiv = maxDiv * base
		exp += 1	
	return [maxDiv, exp]
	
# Retourne un tableau des valeurs
def decToBase(base, decNumber):
	hexVals = []
	divExp = getMaxDiv(base, decNumber)
	maxDiv = divExp[0]
	exp = divExp[1]
	divRes = decNumber
	while( divRes/maxDiv > 0 ): 
		hVal = int(divRes/maxDiv);
		divRes = divRes - ( hVal*maxDiv );
		maxDiv = maxDiv/base;
		hexVals.append( hVal )
			
	for ie in range( len(hexVals)-1, exp):
		hexVals.append( 0 )

	return hexVals; 

def decToHex(dec): 
	return decToBase(16, dec)
	
def decToBin(dec): 
	return decToBase(2, dec)
	

# Conversions

def hexToBibi ( hexNumber ):
	phonetic = ''
	for h in hexNumber:
		phonetic += bibiPhonetic[h]
	return phonetic

def decToBibi(decNum):
	return hexToBibi(decToHex( decNum ))
	
# Un symbole pouvant contenir jusqu'à 4 caractères, on sépare par un point.
def hexToAscii ( hexNumber ):
	s = ''
	n=0
	for h in hexNumber:
		s += notationAscii[h]
		if n < len(hexNumber)-1:
			s += '.'
		n += 1
	return s
	
	
def decToStr(dec): 
	bina = decToBin(dec) 
	strBin = '000'
	for i in bina:
		strBin += str(i)
	return strBin[-4:]
	
def decToClockStr(dec):
	s = decToStr(dec)
	sqS = ''
	sqS += s[3]+'   '+s[0]+'\n'
	sqS += asciiArrows[1]+'   '+asciiArrows[4]+'\n'
	sqS += s[2]+ asciiArrows[2] +s[1]
	return sqS
	






