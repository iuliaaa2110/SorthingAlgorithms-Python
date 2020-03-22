g = open("date.in", "w")
import random

#1: vector sortat descrescator cu elementele de la 10^5 la 1
for i in range(100000, 1, -1):
    g.write(str(i) + " ")
g.write('\n')

#3: vector cu elemente de pana la 10^1000
for i in range(1,1000):
    c = pow(10, i)
    g.write(str(random.randint(10, c)) + " ")
g.write('\n')

#2: vector cu elemente negative
for i in range(50):
    g.write(str(-i)+" "+str(i)+" ")
g.write('\n')

#4: vector cu elemente egale
for i in range(50):
    g.write(str(9999999)+" ")
g.write('\n')

#5: vector sortat crescator
for i in range(1000):
    g.write(str(i) + " ")
g.write('\n')
