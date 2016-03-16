def insertionSort(alist):
    karsilastirma=0
    yerdegistirme=0
    girdi= False
    for index in range(1,len(alist)):
    
        currentvalue = alist[index]
        position = index
        girdi= False
        while position>0 and alist[position-1]>currentvalue:
             yerdegistirme=yerdegistirme+1
             karsilastirma=karsilastirma+1
             alist[position]=alist[position-1]
             position = position-1
             girdi= True
   
        if girdi == False:
            karsilastirma=karsilastirma+1
            girdi = True
        alist[position]=currentvalue
    print("karsılastırma sayısı : ",karsilastirma)
    print("yerdegistirme sayısı : ",yerdegistirme)

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
insertionSort(alist)
#bubbleSort(alist)
t_end=time.time()

for i in range(0,len(alist)):
    print(i, ".item",alist[i])
print("n kare: ",size*size, "time : " ,t_end-t_start)
