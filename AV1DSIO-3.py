import math as m

a = int(input('Unesi stranicu a trokuta: '))
b = int(input('Unesi stranicu b trokuta: '))
c = int(input('Unesi stranicu c trokuta: '))

S = (a+b+c)/2

R = m.sqrt(S*(S-a)*(S-b)*(S-c))

print('Povrsina trokuta je: {:6.2f}'.format(R))
