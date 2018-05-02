



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
get_ipython().magic('matplotlib inline')
#os.chdir('D:\CESAR')
#plt.style.use('ggplot')


# In[2]:


df = pd.read_csv('/home/All_coordenates/para_python2.csv')
# Eliminando el indice repetido debido a los chunks
#df = df.drop(df.columns[0], axis=1)
# Tranforando el time stamp 
df.TIMESTAMP=df.TIMESTAMP + (df.TRAYECTORY_ID*15)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], unit='s')


# In[6]:


# Obteniendo la variable de la hora y los conteos de incios de viajes y finales de viajes por cluster por hora
df['HORA'] = df.TIMESTAMP.dt.hour
start = df.groupby(['cluster','HORA'])['START_FLAG'].sum()
end = df.groupby(['cluster','HORA'])['END_FLAG'].sum()
#df.to_csv('checkpoint5.csv')


# In[7]:


# Ahora voy a estimar la velocidad promedio por cluster
# El primer paso es determinar las trayectorias completas en el cluster 
# Usando funciones lag para tal fin 
df['LAG_TRAYECTORY_ID'] = df.groupby(['cluster','TRIP_ID'])['TRAYECTORY_ID'].shift(1)
# Solo necesito el subconjunto que describe una trayectoría
df = df.loc[(df.TRAYECTORY_ID-df.LAG_TRAYECTORY_ID)==1]


# In[8]:


df.to_csv('checkpoint7.csv')


# In[10]:


# Lags sobre las longitudes para poder cálcular distancias ya que se necesita sobre dos nodos adyacentes
df['LAG_LONG'] = df.groupby(['cluster','TRIP_ID'])['LONGITUD'].shift(1)
df['LAG_LAT'] = df.groupby(['cluster','TRIP_ID'])['LATITUD'].shift(1)
#------------------------------- 
# NOTA: Pierdo una observación para la estimación de la velocidades, 
# pero esto no implica que no la use para sacar datos de los cluesters
#-------------------------------


# In[11]:


# Listo para cálcular distancias de la trayectoría utilizando distancia esferica entre coordenadas
def haversine_np(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km
df['DISTANCIA'] = haversine_np(df.LAG_LONG, df.LAG_LAT,df.LONGITUD, df.LATITUD)


# In[12]:


# Listo para cálcular la velocidad en km/h distanciakm/15/3600
df['VELOCIDAD'] =df['DISTANCIA']/0.00416666666


# In[13]:


df.to_csv('checkpoint12.csv')


# In[18]:


# Obteniendo la velocidad promedio del cluester
velocidad_promedio_cluster=df.groupby(['cluster'])['VELOCIDAD'].mean()


# In[15]:


to_plot=df.groupby(['cluster','HORA'])['VELOCIDAD'].mean()
print(to_plot)


# In[16]:


type(to_plot)


# In[17]:


to_plot.to_csv('velocidad_hora_cluster.csv')


# In[19]:


velocidad_promedio_cluster.to_csv('velocidad_promedio_cluster.csv')


# In[22]:


start.to_csv('start.csv')


# In[23]:


end.to_csv('end.csv')


# In[5]:




