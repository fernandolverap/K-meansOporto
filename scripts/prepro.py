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


data = pd.read_csv('train.csv')


#Eliminando datos con cordenadas faltantes
data = data.loc[data.MISSING_DATA==False]
data = data.loc[data['POLYLINE'] != "[]"]
data.shape
#---------------------------
# Nota:  Se tienen 1,710,660 viajes de un años el manejo se vuelve inviable localmente debido a que cada viaje tiene mas de una 
#        coordenada (columna "POLYLINE").
#--------------------------
data.to_csv('train_womissings.csv')


# Pre - Procesamiento por Chunks se guardarán aproximadamente 17 archivos
chunksze   = 10000
count = 0
for chunk in pd.read_csv('train_womissings.csv', chunksize=chunksze):
        count+=1
        file_name = "all_coordinates_"+str(count)+".csv"
        print (time.ctime())
        str_arr = np.array(chunk[['POLYLINE','DAY_TYPE','TIMESTAMP','TAXI_ID','TRIP_ID']])
        def lambdaf(x):
            y=np.matrix(x[0])
            y=y.reshape(int(y.shape[1]/2),2)
            day_type = np.array(y.shape[0]*[ord(x[1])])
            timestamp = np.array(y.shape[0]*[x[2]])
            taxi_id = np.array(y.shape[0]*[x[3]])
            trip_id = np.array(y.shape[0]*[x[4]])
            trayectory_id = np.arange(y.shape[0])
            start_flag = np.zeros(y.shape[0])
            end_flag = np.zeros(y.shape[0])
            start_flag[0] = 1
            end_flag[y.shape[0]-1] = 1
            x = np.column_stack((y,day_type,timestamp,taxi_id,trip_id,trayectory_id,start_flag ,end_flag))
            return x
        all_coordinates = np.concatenate([lambdaf(x) for x in str_arr])
        print (time.ctime())
        df=pd.DataFrame(all_coordinates,columns=['LATITUD','LONGITUD','DAY_TYPE','TIMESTAMP',
                                         'TAXI_ID','TRIP_ID','TRAYECTORY_ID','START_FLAG','END_FLAG'])
        print (file_name +" *DONE* ")
        df.to_csv(file_name)





