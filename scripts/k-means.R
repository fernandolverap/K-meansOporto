library(readr)

all_data_kmeans <- read_csv("/home/fernando/All_coordenates/all_data_kmeans.csv")

grupos<-kmeans(all_data_kmeans,8)

write.csv(grupos$cluster, file = "/home/fernando/All_coordenates/grupos.csv")
