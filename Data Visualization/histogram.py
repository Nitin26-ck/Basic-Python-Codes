import matplotlib.pyplot as plt
ages=[23,34,43,48,56,45,36,25,46,27,41]
bins=[0,10,20,30,40,50,60,70,80,90]
plt.hist(ages,bins,histtype='bar',color='green',rwidth=0.8)
plt.xlabel('ages of employees')
plt.ylabel=('salaries of employees')
plt.title('CLOWN MONSTERS')
plt.show()