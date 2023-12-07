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
hadoop fs -ls /user/fran                          #Listar los archivos subidos a hadoop
hadoop fs -mkdir /directorio/prueba1              #Crear directorio en hadoop
hadoop fs -put dataset1.txt /directorio/prueba1    #Listar los archivos subidos a hadoop
```

# Ejecutar en Hadoop:
```
python3 mr_prueba.py -r hadoop hdfs:///directorio/prueba1/dataset1.txt
python3 mr_word_count.py -r hadoop hdfs:///user/fran/newdir/input.txt -output=/user/fran    #Guardar el resultado en un fichero
hadoop fs -cat input.txt /user/fran/newdir                                                            #Mostrar el fichero
```


hadoop dfsadmin -safemode leave
