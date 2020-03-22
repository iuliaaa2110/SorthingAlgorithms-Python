g = open("date.in", "w")
import random
#1: vector sortat descrescator cu elementele de la 10^17
for i in range(100, 1, -1):
    g.write(str(i*1000000000000000) + " ")
g.write('\n')

#2: vector cu elemente negative
for i in range(100):
    g.write(str(-i)+" ")
g.write('\n')
#3: vector cu elemente de pana la 10^100
for i in range(1,100):
    c = pow(10, i)
    g.write(str(random.randint(10, c)) + " ")
g.write('\n')

#4: vector cu elemente egale
for i in range(100):
    g.write(str(9999999)+" ")
g.write('\n')
#5: vector sortat crescator cu elementele de la 1 la 10^6
for i in range(100):
    g.write(str(i) + " ")