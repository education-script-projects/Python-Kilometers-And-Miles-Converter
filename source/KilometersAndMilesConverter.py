#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

kilometers_to_miles_ico = """
##########################################################
# PYTHON - Kilometers & Miles Converter - GH0ST S0FTWARE #
########################################################## 
#                       CONTACT                          #
##########################################################
#              DEVELOPER : İSMAİL TAŞDELEN               #
#           GMAIL : pentestdatabase@gmail.com            #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen  #
#           Whatsapp : + 90 534 295 94 31                #
########################################################$#
"""

print kilometers_to_miles_ico

star = "#########################################################"

def kilometreden_mile():
	print star
	kilometre = input("Kaç kilometre ? : ")
	print star
	formul = 1.609344
	mil = kilometre / formul
	print("%0.3f kilometre %0.3f mile eşittir." %(kilometre,mil))
	print star

def milden_kilometreye():
	print star
	kilometre = input("Kaç kilometre ? : ")
	print star
	formul = 1.609344
	mil = kilometre * formul
	print("%0.3f mil %0.3f kilometreye eşittir." %(kilometre,mil))
	print star

print star

islemler_ico = """
(1) Kilomtreden mile çevir.
(2) Milden kilomtreye çevir.
(3) Çıkış yap.
"""

print islemler_ico

print star

islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")

if islem == 1:
	kilometreden_mile()
elif islem == 2:
	milden_kilometreye()
elif islem == 3:
	sys.exit()
