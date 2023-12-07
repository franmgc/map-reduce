# -- LOCAL --- 
```
python3 mr.py dataset.csv 
```




# -- HADOOP -- 
```
hdfs namenode -format

start-all.sh
jps
stop-all.sh
```

# Subir fichero a hadoop:
```
hadoop fs -mkdir /directorio/mrjob-v1              #Crear directorio en hadoop
hadoop fs -ls /directorio/mrjob-v1                 #Listar los archivos subidos a hadoop
hadoop fs -put dataset.csv /directorio/mrjob-v1    #Listar los archivos subidos a hadoop
```

# Ejecutar en Hadoop:
```
python3 mr.py -r hadoop hdfs:///directorio/mrjob-v1/dataset.csv
python3 mr.py -r hadoop hdfs:///directorio/mrjob-v1/dataset.csv -output=/directorio/mrjob-v1             #Guardar el resultado en un fichero
hadoop fs -cat <fichero>.txt /directorio/mrjob-v1/dataset.csv                                            #Mostrar el fichero
```


hadoop dfsadmin -safemode leave


# -- EMR --

```
# crear un cluster
mrjob create-cluster -c emr.conf

# ejecutar en el cluster
fran@virtualbox:~/gonzalez/progra/TA$ python3 mr.py -r emr --cluster-id j-ALU8JIJ72J37 --region us-east-1 s3://datasets.elasticmapreduce/ngrams/books/ -c /home/fran/emr.conf

```



