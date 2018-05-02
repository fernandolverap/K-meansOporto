# Importando algunas librerias a utilizar
import time
import numpy as np
import pandas as pd
import sys
import pandas as pd
import numpy  as np
import scipy.io
import random 
import os
import matplotlib
import matplotlib.pyplot as plt
from datetime import timedelta
from scipy.stats import gaussian_kde
from matplotlib import rc
from datetime import datetime
from dateutil.parser import parse
from dateutil.parser import parse
import matplotlib as mpl
from dateutil.relativedelta import relativedelta
import copy
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.colors import LogNorm
from scipy.spatial.distance import pdist, squareform
%matplotlib inline
#os.chdir('D:\CESAR')
#plt.style.use('ggplot')






df = pd.read_csv('/home/All_coordenates/para_python2.csv')
# Eliminando el indice repetido debido a los chunks
#df = df.drop(df.columns[0], axis=1)
# Tranforando el time stamp 
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], unit='s')


# Aplicando K-means
kmeans = KMeans(n_clusters=8, random_state=0).fit(df[['LONGITUD','LATITUD']])
df['CLUSTER']= kmeans.labels_
df.head(5)
