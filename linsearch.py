from array import *
a=array('i',[])
n=int(input('enter n'))
for i in range(n):
    print('enter element:',end='')
    a.append(int(input()))
print('original array is:',a)
s=int(input('enter element to search'))
flag=False
for i in range(len(a)):
    if s==a[i]:
        print('element is present and is at position',i+1)
        flag=True
if flag==False:
    print('element is not found')
