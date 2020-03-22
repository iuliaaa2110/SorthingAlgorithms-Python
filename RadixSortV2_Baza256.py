
import time

def RadixSort256(v):
    s = 0
    m = (1 << 8) - 1    #pt ca am 256
    maxim = max(v)
    cc= 0
    while maxim > 0:
        maxim >>= 8
        cc += 1
    for i in range(cc):
        bucket=[[] for j in range(256)]
        for j in v:
            x = (j >> s) & m
            bucket[x].append(j)
        v = []
        for j in range(256):
            v.extend(bucket[j])
        s += 8
    return v

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
        if okp and okp2 :

            # radix sort:
            l=RadixSort256(l)

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
#lista de lungime <=10^5
