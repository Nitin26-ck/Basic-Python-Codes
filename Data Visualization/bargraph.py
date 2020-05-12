import matplotlib.pyplot as plt
x=[1001,1002,1003,1004,1005,1006]
y=[45000,34000,24000,47000,26000,38000]
plt.bar(x,y,label='sales dept',color='red')
plt.xlabel('emp id')
plt.ylabel('salaries')
plt.title('my bar')
plt.legend()
plt.show()