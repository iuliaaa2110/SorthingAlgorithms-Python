import time
def BubbleSort():
    global l
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                aux = l[j]
                l[j] = l[j + 1]
                l[j + 1] = aux

#citire/main
f = open("date.in")
for k in range (5):
    start_time = time.time()
    l = []
    l = f.readline().split()
    for i in range(len(l)):
        l[i]=int(l[i])
    BubbleSort()

    # verificare ca sorteaza corect:

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

#pe liste de mai putin de 10000 de numere! Altfel ajunge la 20 de secunde
#asa are maxim 0.30 secunde
#pe numere oricat de mari
#merge si pe numere negative