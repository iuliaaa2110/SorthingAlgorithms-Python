import time
import random

def partitie(l, st, dr):
    k = st - 1
    poz=random.randint(st,dr)
    l[dr],l[poz]=l[poz],l[dr]
    p = l[dr]  # =pivotul!!
    for i in range(st, dr):
        if l[i] < p:  # pun elementele mai mici in stanga si cele mai mari in dreapta
            k += 1
            l[i], l[k] = l[k], l[i]
    l[k + 1], l[dr] = l[dr], l[
        k + 1]  # k reprezinta pozitia ultimului element mai mic decat pivot,deci acum o sa pun pivotul pe k+1 ca sa fie la mijloc intre elem mai mici si cele mai mari decat el
    return k + 1  # returnez pozitia care este acum a pivotului


def quicksort(l, st, dr):
    if st < dr:  # mai am elem de verificat
        m = partitie(l, st, dr)
        quicksort(l, st, m - 1)
        quicksort(l, m + 1, dr)


def gresit():
    print("sortarea nu este corecta")


f = open("date.in")
g = open("date.out", "w")

for k in range(5):
    start_time = time.time()
    l = []
    l = f.readline().split()
    print('\n')
    print("lista ", str(k + 1),":")
    if len(l)>100:
        print("Programul nu sorteaza mai mult de 100 de elemente")
    else:
        for i in range(len(l)):
            l[i] = int(l[i])

        n = len(l) - 1
        quicksort(l, 0, n)

        # verificare ca sorteaza corect:
        i = 0
        ok = 0
        while i < n and ok == 0:
            if l[i] > l[i + 1]:
                ok = 1
            i += 1
        if ok == 1:
            print(l)
            gresit()
        else:
            print(l)
    print("--- %s seconds ---" % (time.time() - start_time))

#limita nr de elemente: 100 pentru a evita RecursionError: maximum recursion depth exceeded in comparison
#elementele pot sa fie oricat de mari, fiind doar o suta le sorteaza oricum in aproximativ 0,01 secunde
#elementele pot fi si negative, nu e nicio problema
