# pseudocode 
# create a list to store data
costs=[1,8,15,7,5,14,43,40]
# cities=['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']
dictionary={'Los Angeles 1984':1, 'Seoul 1988':8, 'Barcelona 1992':15, 'Atlanta 1996':7, 'Sydney 2000':5, 'Athens 2003':14, 'Beijing 2008':43, 'London 2012':40}
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: int(x[1])))
print(sorted_dict.values())
import numpy as np
import matplotlib.pyplot as plt
# creat the x,y ticks of the bar plot
plt.ylabel('costs')
plt.title('Olympic Costs')
plt.xlabel('cities')
plt.bar(sorted_dict.keys(),sorted_dict.values(),0.5)
plt.yticks(np.arange(0,45,5))
plt.show()
