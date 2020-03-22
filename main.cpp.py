import time
import random
f = open("date.in")
g = open("date.in", "w")

def Verificare_sortare_corecta(l):
    i = 0
    ok = 0
    while i < len(l) - 1 and ok == 0:
        if l[i] > l[i + 1]:
            ok = 1
        i += 1
    if ok == 1:
        return False
    return True

#1:
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

#2:
def partitie(l, st, dr):
    k = st - 1
    poz = random.randint(st, dr)
    l[dr], l[poz] = l[poz], l[dr]
    p = l[dr]  # =pivotul!!
    for i in range(st, dr):
        if l[i] < p:  # pun elementele mai mici in stanga si cele mai mari in dreapta
            k += 1
            l[i], l[k] = l[k], l[i]
    l[k + 1], l[dr] = l[dr], l[k + 1]  # k reprezinta pozitia ultimului element mai mic decat pivot,deci acum o sa pun pivotul pe k+1 ca sa fie la mijloc intre elem mai mici si cele mai mari decat el
    return k + 1  # returnez pozitia care este acum a pivotului


def quicksort(l, st, dr):
    if st < dr:  # mai am elem de verificat
        m = partitie(l, st, dr)
        quicksort(l, st, m - 1)
        quicksort(l, m + 1, dr)


def gresit():
    print("sortarea nu este corecta")

#3:
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


#4:
def merge_lists(lst, ldr):
    i = j = 0

    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1

    rez.extend(lst[i:])
    rez.extend(ldr[j:])

    return rez


def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        mij = len(ls) // 2
        lst = merge_sort(ls[:mij])
        ldr = merge_sort(ls[mij:])
        return merge_lists(lst, ldr)

#5:
def BubbleSort():
    global l
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                aux = l[j]
                l[j] = l[j + 1]
                l[j + 1] = aux




#1: mainCountSort:
def Tasta1():
    #a)Generator de inputuri:
    #1: vector sortat descrescator cu elementele de la 10^6 la 1
    for i in range(1000000, 1, -1):
        g.write(str(i) + " ")
    g.write('\n')

    #2: vector cu elemente negative
    for i in range(10000):
        g.write(str(-i)+" ")
    g.write('\n')
    #3: vector cu elemente mai mari decat 10^7
    for i in range(1,20):
        c = pow(10, i)
        g.write(str(random.randint(10, c)) + " ")
    g.write('\n')

    #4: vector cu 10^10 elemente egale
    for i in range(1000):
        g.write(str(9999999)+" ")
    g.write('\n')
    #5: vector sortat crescator cu elementele de la 1 la 10^6
    for i in range(1000000):
        g.write(str(i) + " ")

    #b)Citiri/apelari/afisari/Verificari:
    print("~CountSort~")
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
            if Verificare_sortare_corecta(l):
                print(l)
            else:
                print(l)
                print("sortarea nu este corecta")
        print("--- %s seconds ---" % (time.time() - start_time))

        # Lista de 10^7 elemente deja sortate crescator: 22.48 secunde
        # 20 secunde mi s-a parut chiar mult, asa ca am pus limita sa fie mai mici de 10^7
        # 10^6 numere sortate descrescator: 4,03/ 5.97
        # merge pe liste cu un singur element/pe liste goale
        # parcurgerea vectorului se opreste imediat ce intalneste un nr negativ sau <10^7. Pe exemplul dat: 0.01 secunde
        # pe o lista cu elemente egale:3.71 sec
        # 10^6 elemente sortate crescator de la 1 la 10^6: 4.11 secunde



def Tasta2():
    #2: QuickSort
    #a)Generator de input

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

    #b)Citiri/apelari/afisari/Verificari:
    print("~Quicksort~")
    for k in range(5):
        start_time = time.time()
        l = []
        l = f.readline().split()
        print('\n')
        print("lista ", str(k + 1), ":")
        if len(l) > 100:
            print("Programul nu sorteaza mai mult de 100 de elemente")
        else:
            for i in range(len(l)):
                l[i] = int(l[i])

            n = len(l) - 1
            quicksort(l, 0, n)

            # verificare ca sorteaza corect:
            if Verificare_sortare_corecta(l):
                print(l)
            else:
                print(l)
                print("sortarea nu este corecta")
        print("--- %s seconds ---" % (time.time() - start_time))

    # limita nr de elemente: 100 pentru a evita RecursionError: maximum recursion depth exceeded in comparison
    # elementele pot sa fie oricat de mari, fiind doar o suta le sorteaza oricum in aproximativ 0,01 secunde
    # elementele pot fi si negative, nu e nicio problema


def Tasta3():
    #3:RadixSort:
    #a)Generator de input:

    #1: vector sortat descrescator cu elementele de la 10^5 la 1
    for i in range(100000, 1, -1):
        g.write(str(i) + " ")
    g.write('\n')

    #3: vector cu elemente de pana la 10^100
    for i in range(1,100):
        c=pow(10,i)
        g.write(str(random.randint(10,c))+" ")
    g.write('\n')

    #2: vector cu elemente negative
    for i in range(200):
        g.write(str(-i)+" "+str(i)+" ")
    g.write('\n')

    #4: vector cu elemente egale
    for i in range(200):
        g.write(str(9999999)+" ")
    g.write('\n')

    #5: vector sortat crescator cu elementele de la 1 la 10^6
    for i in range(100000):
        g.write(str(i) + " ")
    g.write('\n')


    #b) Citiri/Apelari/Afisari/Verificari:
    print("~Radixsort~")
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
                if Verificare_sortare_corecta(l):
                    print(l)
                else:
                    print(l)
                    print("sortarea nu este corecta")
        print("--- %s seconds ---" % (time.time() - start_time))

    #numere mai mici de 10^100, altfel ajunge la 11 sec pe un vector sortat
    #lista de lungime <=10^5


def Tasta4():
    #4:Mergesort:

    #a)Generator de input:
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


    #b)citiri/apelari/verificari/afisari:
    for k in range(5):
        start_time = time.time()
        ls=f.readline().split()
        print('\n')
        print("lista",str(k+1),":")
        print("nr de elemente=", str(len(ls)))
        if len(ls)>=1000000:
            print("Programul nu sorteaza mai mult de 1000000 elemente")
        else:
            for i in range(len(ls)):
                ls[i] = int(ls[i])
            ls = merge_sort(ls)
            #verificare:
            if Verificare_sortare_corecta(l):
                print(l)
            else:
                print(l)
                print("sortarea nu este corecta")
        print("--- %s seconds ---" % (time.time() - start_time))

    #limita de 10^5 numere
    #numerele pot sa fie oricat de mari
    #merge si pe numere negative
    #ajunge la 0.5 secunde pe cazul in care vectorul este deja sortat


def Tasta5():
    #5:Main Bubblesort:

    #a)Generator de inputuri:
    #1: vector sortat descrescator cu elementele de la 10^5 la 1
    for i in range(1000, 1, -1):
        g.write(str(i) + " ")
    g.write('\n')

    #3: vector cu elemente de pana la 10^1000
    for i in range(1,1000):
        c = pow(10, i)
        g.write(str(random.randint(10, c)) + " ")
    g.write('\n')

    #2: vector cu elemente negative
    for i in range(200):
        g.write(str(-i)+" "+str(i)+" ")
    g.write('\n')

    #4: vector cu elemente egale
    for i in range(200):
        g.write(str(9999999)+" ")
    g.write('\n')

    #5: vector sortat crescator cu elementele de la 1 la 10^6
    for i in range(1000):
        g.write(str(i) + " ")
    g.write('\n')


    #b)main
    print("~Bubblesort~")
    for k in range (5):
        print('\n')
        print("lista", str(k + 1), ":")
        print("nr de elemente=", str(len(ls)))
        start_time = time.time()
        l = []
        l = f.readline().split()
        for i in range(len(l)):
            l[i]=int(l[i])
        BubbleSort()
        # verificare ca sorteaza corect:
        if Verificare_sortare_corecta(l):
            print(l)
        else:
            print(l)
            print("sortarea nu este corecta")
        print("--- %s seconds ---" % (time.time() - start_time))

    #pe liste de mai putin de 10000 de numere! Altfel ajunge la 20 de secunde
    #asa are maxim 0.30 secunde
    #pe numere oricat de mari
    #merge si pe numere negative


#main()
print("Apasa tasta corespunzatoare sortarii pe care doresti sa o vezi (CountSort=Tasta 1, Quicksort=Tasta 2, Radixsor=Tasta 3, Mergesort=Tasta 4, Bubblesort=Tasta 5)")
t=int(input("tasta="))
if t==1:
    Tasta1()
if t==2:
    Tasta2()
if t==3:
    Tasta3()
if t==4:
    Tasta4()
if t==5:
    Tasta5()
