import time
from random import randrange
def boubllesort(l):
    ok = 0
    while ok == 0:
        ok = 1
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                (l[i], l[i + 1]) = (l[i + 1], l[i])
                ok = 0
    return l
def countsort(l):
    d=[0]*(max(l)+1)
    for i in l:
        d[i]+=1
    t=[]
    for i in range(len(d)):
        for j in range(d[i]):
            t.append(i)
    return t
def piv(l,st,dr):
    x=randrange(len(l))
    i=st-1
    for j in range(st,dr):
        if l[j]<x:
            i+=1
            (l[i],l[j])=(l[j],l[i])
    (l[i+1],l[dr])=(l[dr],l[i+1])
    return i+1
def qsort(l,st,dr):
    if st<dr:
        n=piv(l,st,dr)
        qsort(l,st,n-1)
        qsort(l,n+1,dr)
    return l
def interclasare(lst,ldr):
    i=j=0
    rez=[]
    while i<len(lst) and j<len(ldr):
        if lst[i]<=ldr[j]:
            rez.append(lst[i])
            i+=1
        else:
            rez.append(ldr[j])
            j+=1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez
def mergesort(ls):
    if len(ls)<=1 :
        return ls
    else:
        mij=len(ls)//2
        lst=mergesort(ls[:mij])
        ldr=mergesort(ls[mij:])
        return interclasare(lst,ldr)

def sortcifre(v, p):
    n = len(v)
    l = [0] * n
    nr = [0] * 10
    for i in range(n):
        cif = v[i] // p
        nr[int(cif) % 10] += 1
    for i in range(1, 10):
        nr[i] += nr[i - 1]
    i = n - 1
    while i >= 0:
        cif = v[i] // p
        l[nr[int(cif) % 10] - 1] = v[i]
        nr[int(cif) % 10] -= 1
        i -= 1
    i = 0
    return l
def radixSortb2(v):
    m = max(v)
    p = 1
    while m //p > 0:
        v=sortcifre(v, p)
        p *= 2
    return v
def radixSortb4(v):
    m = max(v)
    p = 1
    while m //p > 0:
        v=sortcifre(v, p)
        p *= 4
    return v
def test():
    f=open("date.out")
    oka=okb=okc=okd=oke=okf=1
    for i in f.readlines():
        l=[]
        i=i[:-1].split(" ")
        for x in i:
            l.append(int(x))
        start=time.time()
        a=boubllesort(l)
        stop=time.time()
        at=stop-start
        start=time.time()
        b=countsort(l)
        stop = time.time()
        bt=stop-start
        start = time.time()
        c=qsort(l,0,len(l)-1)
        stop = time.time()
        ct=stop-start
        start = time.time()
        d=mergesort(l)
        stop = time.time()
        dt = stop - start
        start=time.time()
        e = radixSortb2(l)
        stop = time.time()
        et=stop-start
        start = time.time()
        f = radixSortb4(l)
        stop = time.time()
        st = stop - start
        start = time.time()
        l.sort()
        stop=time.time()
        ft=stop-start
        print("Lista sortata este",l," cu timpul de ",int(ft)," secunde")
        if l!=a:
            oka=0
        if l!=b:
            okb=0
        if l!=c:
            okc=0
        if l!=d:
            okd=0
        if l!=e:
            oke=0
        if l!=f:
            okf=0
        if oka==1:
            print("Boublesort merge cu ",int(at*1000)," milisecunde")
        else:
             print("Boublesort nu merge")
        if okb==1:
            print("Countsort merge cu " ,int(bt*1000)," milisecunde")
        else:
            print("Countsort nu merge")
        if okc==1:
            print("Quicksort merge cu ",int(ct*1000)," milisecunde")
        else:
            print("Quicksort nu merge")
        if okd==1:
            print("Mergesort merge cu ",int(dt*1000)," milisecunde")
        else:
            print("Mergesort nu merge")
        if oke==1:
            print("Radixsort in baza 2 merge cu ",int(et*1000)," milisecunde")
        else:
            print("Radixsort in baza 2 nu merge")
        if okf==1:
            print("Radixsort in baza 4 merge cu ",int(st*1000)," milisecunde")
        else:
            print("Radixsort in baza 4 nu merge")
test()