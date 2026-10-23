#This is where the computer conducts its identification of the genes
from 23_COnvert.py import convert_file_to_23

genes = convert_file_to_23

from sklearn.cluster import KMeans
import numpy as np

#  genes : [Base 1, Base 2]
genes = np.array([[x, y], [x, y], [x, y], [x, y], [x, y], [x, y]])

# Tell the computer to find 3 distinct patterns/groups
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(genes)

# See which group each data point belongs to
print(kmeans.labels_) 
# Output might look like: [0, 0, 1, 1, 2, 2] (3 clear patterns detected)
