import sys
n=len(sys.argv)
args=sys.argv
print('no of command line args=',n)
print('the args are',args)
print('args one by one:')
for a in args:
    print(a)
