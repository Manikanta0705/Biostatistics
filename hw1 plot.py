import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'Polar':5, 'Non-Polar':10, 'Charged':5,
        'Aromatic':4 ,'Essential':9, 'Non-Essential':11}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color =['C0','C1','C2','C3','C4','C5','C6'],
        width = 0.3)
 
plt.xlabel("Different categories of amino acids")
plt.ylabel("No. of amino acids")
plt.title("Classification of amino acids")
plt.show()