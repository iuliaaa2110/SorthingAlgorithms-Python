import time
def Count_Sort(p):
    global l
    c = [0] * 10
    v = [0] * len(l)
    for i in l:
        c[i // p % 10] += 1
    for i in range(1, 10):
        c[i] += c[i - 1]
    i = len(l) - 1
    while i >= 0:
        v[c[l[i] // p % 10] - 1] = l[i]
        c[l[i] // p % 10] -= 1
        i -= 1
    for i in range(len(l)):
        l[i] = v[i]


f = open("date.in")
for k in range(5):
    start_time = time.time()
    l = []
    l = f.readline().split()
    print('\n')
    print("lista", str(k + 1), ":")
    print("nr de elemente=", str(len(l)))
    if len(l)>100000:
        print("Programul nu sorteaza mai mult de 10^5 elemente")
    else:
        okp=1
        okp2=1
        for i in range(len(l)):
            l[i] = int(l[i])
            if l[i]>=pow(10,1000):
                okp=0
                break
            if l[i]<0:
                okp2=0
                break
        if okp2==0:
            print("Programul nu sorteaza si elemente negative")
        if okp==0:
            print("Programul nu sorteaza elemente mai mari decat 10^100")
        if okp and okp2:
            # radix sort:
            maxim = max(l)
            p = 1
            while maxim >= p:
                Count_Sort(p)
                p *= 10

            #verificare:
            i = 0
            ok = 0
            while i < len(l)-1 and ok == 0:
                if l[i] > l[i + 1]:
                    ok = 1
                i += 1
            if ok == 1:
                print(l)
                print("sortarea nu este corecta")
            else:
                print(l)
    print("--- %s seconds ---" % (time.time() - start_time))

#numere mai mici de 10^100, altfel ajunge la 11 sec pe un vector sortat
#lista de lungime >10^5, pt 10^6 ar ajunge la 7 secunde. Asa nu depaseste 2 sec
