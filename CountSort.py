import time

def CountSort():
    global l
    c = [0] * 10000000
    for i in range(len(l)):
        l[i] = int(l[i])
        c[l[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    v = [0] * len(l)
    for i in range(len(l)):
        v[c[l[i]] - 1] = l[i]
        c[l[i]] -= 1
    return v


# main:
f = open("date.in")
for k in range(5):
    start_time = time.time()
    print('\n')
    print("lista ",k+1)
    l = []
    okp1=1
    okp2=1
    l = f.readline().split()
    print("nr de elemente=",len(l))
    for i in range(len(l)):
        l[i]=int(l[i])
        if l[i]<0:
            okp1=0
            break
        if l[i]>1000000:
            okp2=0
            break
    if okp1==0:
        print("CountingSort nu sorteaza numere negative!")
    if okp2==0:
        print("Counting Sort nu sorteaza numere mai mari decat 10^7")
    if okp1 and okp2:
        l = CountSort()

        # verificare ca sorteaza corect:
        i = 0
        ok = 0
        while i < len(l) - 1 and ok == 0:
            if l[i] > l[i + 1]:
                ok = 1
            i += 1
        if ok == 1:
            print(l)
            print("sortarea nu este corecta")
        else:
            print(l)
    print("--- %s seconds ---" % (time.time() - start_time))


#Lista de 10^7 elemente deja sortate crescator: 22.48 secunde
# 20 secunde mi s-a parut chiar mult, asa ca am pus limita sa fie mai mici de 10^7
#10^6 numere sortate descrescator: 4,03/ 5.97
#merge pe liste cu un singur element/pe liste goale
#parcurgerea vectorului se opreste imediat ce intalneste un nr negativ sau <10^7. Pe exemplul dat: 0.01 secunde
#pe o lista cu elemente egale:3.71 sec
#10^6 elemente sortate crescator de la 1 la 10^6: 4.11 secunde