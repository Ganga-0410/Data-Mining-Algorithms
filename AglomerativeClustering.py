#Aglomerative Clustering using Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from scipy.spatial.distance import squareform, pdist

a = [0.40,0.22,0.35,0.26,0.08,0.45]
b = [0.53,0.38,0.32,0.19,0.41,0.30]

point = ['P1','P2','P3','P4','P5','P6']
data = pd.DataFrame({'Point':point, 'a':np.round(a,2), 'b':np.round(b,2)})
data = data.set_index('Point')
print(data)

plt.figure(figsize=(8,5))
plt.scatter(data['a'], data['b'], c='r', marker='*')
plt.xlabel('Column a')
plt.ylabel('column b')
plt.title('Scatter Plot of x and y')
for j in data.itertuples():
plt.annotate(j.Index, (j.a, j.b), fontsize=15)

dist = pd.DataFrame(squareform(pdist(data[['a', 'b']]), 'euclidean'), columns=data.index.valuesp)
print(dist)
                    
plt.figure(figsize=(12,5))
plt.title("Dendrogram with Single inkage")
dend = shc.dendrogram(shc.linkage(data[['a', 'b']], method='single'), labels=data.index)
 
