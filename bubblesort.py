def bubbleSort(alist):
    karsilastirma=0
    yerdegistirme=0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            karsilastirma=karsilastirma+1
            if alist[i]>alist[i+1]:
                yerdegistirme=yerdegistirme+1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    print("karsılastırma sayısı : ",karsilastirma)
    print("yerdegistirme sayısı : ",yerdegistirme)
#alist = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)

def createAnArray(size):
    import random
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-10000,10000)))
       # print(i,".item", array[i])
    return array
size=int(input("size?"))
alist = createAnArray(size)
import time
t_start=time.time()
bubbleSort(alist)
t_end=time.time()

for i in range(0,len(alist)):
    print(i, ".item",alist[i])
print("n kare: ",size*size, "time : " ,t_end-t_start)
