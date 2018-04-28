#bubble Sort
import random as rn

N=int(input('List Size:'))
mylist=[rn.randint(1,100)for k in range(N)]
print('Unsorted List:',mylist)
for k in range(len(mylist)-1,0,-1):
    for i in range(k):
        if mylist[i]>mylist[i+1]:
            temp=mylist[i]
            mylist[i]=mylist[i+1]
            mylist[i+1]=temp

print('Sorted List:',mylist)
            
        
    
