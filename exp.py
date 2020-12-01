n=[int(i) for i in input('enter power of e and no of iterations').split(',')]
t=1
sum=t
print('iteration=%d\t,sum=%f'%(1,sum))
for j in range(1,n):
    t=t*x/j
    sum=sum+t
    print('iteration=%d\t,sum=%f'%(sum,j+1)