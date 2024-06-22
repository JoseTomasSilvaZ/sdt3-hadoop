# 🐘+🐷 +🐝 - Proyecto 3 - Hadoop, Hive & Pig

Este proyecto se centra en el uso de Apache Pig y Apache Hive para analizar los Google Workload Traces con el objetivo de comprender mejor el uso de recursos y los patrones de carga de trabajo en los centros de datos de Google, profundizando la utilización de las tecnologías mencionadas. La implementación y configuración se realizaron utilizando Docker.
Específicamente, el dataset analizado se puede encontrar [haciendo click aquí](<https://console.cloud.google.com/storage/browser/_details/external-traces/charlie/trace-1/17571657100049929577.branch_trace.1006511.csv.gz;tab=live_object?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22.csv_5C_22_22%257D%255D%22,%22s%22:%5B(%22i%22:%22objectMetadata%2Fsize%22,%22s%22:%221%22),(%22i%22:%22displayName%22,%22s%22:%220%22)%5D))>)

## Configuración

#### Clonar el proyecto

```bash
git clone https://github.com/JoseTomasSilvaZ/sdt3-hadoop.git
```

#### Correr el contenedor de Docker

```bash
docker run -it -p 50070:50070 -p 8088:8088 -p 8080:8080 suhothayan/hadoop-spark-pig-hive:2.9.2 bash
```

#### Copiar los archivos de setup, dataset al container

```bash
sudo docker cp pig-scripts <container_id>:/home
sudo docker cp sh <container_id>:/home
sudo docker cp datasets<container_id>:/home
```

#### Ejecutar el setup

```bash
sudo docker exec -it <container_id> bin/bash
cd /home/sh
chmod +x *.sh
./setup-hadoop.sh && ./setup-hdfs.sh && ./setup-psql.sh

```

#### Agregar dataset a HDFS

```bash
hdfs dfs -put datasets/<dataset_name>.csv data
```

Todo listo 🎉

## Authors

- [@josetomassilvaz](https://github.com/JoseTomasSilvaZ)
- [@fcoagp](https://github.com/fcoagp)
