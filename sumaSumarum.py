#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

print('Vjezba 29-02-2020 -> 01-03-2020')
time.sleep(3)
os.system('clear')

#AV1DSIO-0
#----------------------------------
ime = str(input('Unesi ime: '))
prezime = str(input('Unesi prezime: '))

print('Zdravo,', ime, prezime, sep=' ')
#----------------------------------
time.sleep(3)
os.system('clear')

#AV1DSIO-1
#----------------------------------
uCV1 = int(input('Unesi prvu vrijednost: '))
uCV2 = int(input('Unesi drugu vrijednost: '))

# unosCjelobrojneVrijednosti1 = uCV1
# unosCjelobrojneVrijednosti2 = uCV2
# P = povrsina
# O = obim

P = uCV1*uCV2
O = 2*(uCV1+uCV2)

print('Povrsina pravougaonika je:', P)
print('Obim pravougaonika je:', O)
#----------------------------------
time.sleep(3)
os.system('clear')

#AV1DSIO-2
#----------------------------------
import math as m

r = float(input('Unesi poluprecnik kruga: '))

#Povrsina = P
P = m.pow(r, 2)*m.pi
#Obim = O
O = 2*r*m.pi

#fun fact: pi=3.1416...

#ovdje formatiraj P rez
#print "{:10.4f}".format(x)
print('Povrsina kruga je: {:6.2f}'.format(P))
#ovdje formatiraj O rez
print('Obim kruga je: {:6.2f}'.format(O))
#----------------------------------
time.sleep(3)
os.system('clear')

#AV1DSIO-3
#----------------------------------
import math as m

a = int(input('Unesi stranicu a trokuta: '))
b = int(input('Unesi stranicu b trokuta: '))
c = int(input('Unesi stranicu c trokuta: '))

S = (a+b+c)/2

R = m.sqrt(S*(S-a)*(S-b)*(S-c))

print('Povrsina trokuta je: {:6.2f}'.format(R))
#----------------------------------
time.sleep(3)
os.system('clear')

#AV1DSIO-4
#----------------------------------
a = int(input('Prvi unos: '))
b = int(input('Prvi unos: '))

#print prije swapa za test
print(a)
print(b)

a,b=b,a

#print poslije swapa za test
print(a)
print(b)
#----------------------------------
time.sleep(3)
os.system('clear')
