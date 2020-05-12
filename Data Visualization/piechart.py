import matplotlib.pyplot as plt
slices=[15,50,20,25]
depts=['EEE','ISE','ECE','CSE']
cols=['orange','blue','red','green']
plt.pie(slices,labels=depts,colors=cols,startangle=90,explode=(0,0.2,0,0),shadow=True,autopct='%.lf')
plt.title('PLACEMENT')
plt.legend()
plt.show()