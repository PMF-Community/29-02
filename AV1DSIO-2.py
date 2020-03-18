#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
