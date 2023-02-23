import matplotlib.pyplot as plt
import numpy as np
import random

figure, axes=plt.subplots(figsize=(5,3))

x=np.arange(50)
x_years=1950+x

rnd=np.random.randint(0,10,size=(1,x.size)) #??? 0_0

axes.stackplot(x_years,rnd+x,labels=['Eastasia','Eurasia','Oceania'])
axes.set_title('Combined debt growth over time')
axes.set_ylabel('Total debt')
axes.legend(loc='upper left')
axes.set_xlim(xmin=x_years[0],xmax=x_years[-1])
plt.show()