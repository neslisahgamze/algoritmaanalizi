import random
c=0;
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def createArray(size):
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-1000,1000)))
    return array
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
           global c
           c=c+1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
           global c
           c=c+1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
size=int(input("array size: "))
alist1=createArray(size)
alist2=createArray(size)
#print(alist)

#alist = [54,26,93,17,77,31,44,55,20]

import time

t1=time.time()
bubbleSort(alist1)
print("time for bubbleSort: ", time.time()-t1)

t1=time.time()
quickSort(alist2)
print("time for quickSort: ", time.time()-t1)

#quickSort(alist)
print("karsilastirma sayisi: " ,c)
