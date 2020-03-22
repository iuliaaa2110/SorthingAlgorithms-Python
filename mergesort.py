import time
f=open("date.in")
# Mergesort


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

#main:
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
        i = 0
        ok = 0
        while i < len(ls) - 1 and ok == 0:
            if ls[i] > ls[i + 1]:
                ok = 1
            i += 1
        if ok == 1:
            print(ls)
            print("sortarea nu este corecta")
        else:
            print(ls)
    print("--- %s seconds ---" % (time.time() - start_time))

#limita de 10^5 numere
#numerele pot sa fie oricat de mari
#merge si pe numere negative
#ajunge la 0.5 secunde pe cazul in care vectorul este deja sortat