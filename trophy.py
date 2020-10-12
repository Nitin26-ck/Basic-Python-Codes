prev_year=int(input('enter year'))
prev_winner=str(input('enter t1 or t2'))
t1='india'
t2='australia'
new_year=int(input('enter new year'))
print('let m be the no of matches won by t1')
print('let n be the no of matches won by t2')
m={0,1,2,3,4,5}
n={0,1,2,3,4,5}
m1=int(input('enter m'))
n1=int(input('enter n'))
if (m1+n1)>5:
    print('invalid')
elif (m1+n1)<=5:
    if(m1==n1):
        if(prev_winner!=t2):
            print('trophy retained by t1')
        else:
            print('trophy won by t2')
    elif(m1>n1):
        print('t1 won the trophy')
    elif(n1>m1):
        print('t2 won the trophy')
    elif(prev_winner!=(t1 or t2)):
            print('trophy shared') 
else:
    print('exit')
