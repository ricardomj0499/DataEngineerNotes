Primero crear la imagen hadoop base
hadoop_cluster\standalone
docker build -t hadoop:341 -f ./hadoop_cluster/standalone/Dockerfile ./hadoop_cluster/standalone

Correr el pseudo
docker build -t pseudo:341 .\hadoop_cluster\pseudo_distributed\

docker build -t worker-node:341 .\hadoop_cluster\full_distributed\worker_node\

docker build -t master-node:341 .\hadoop_cluster\full_distributed\master_node\

docker network create hadoop-network

docker volume create master-data

docker volume create worker-data-1

docker volume create worker-data-2

docker run -d --cap-add=sys_nice -p 9870:9870/ -p 8088:8088 -p 9000:9000 -p 8020:8020 --network hadoop-network --volume master-data:/opt/hdfs_data/data --name master-node master-node:341
9000

8042 nmodde agregapar port

docker run -d --cap-add=sys_nice --network hadoop-network -p 9864:9864 -p 8042:8042 --volume worker-data-1:/opt/hdfs_data/data --name worker-node-1 worker-node:341

-p 9866:9866

docker run -d --cap-add=sys_nice --network hadoop-network -p 9865:9864 -p 9867:9866 -p 8043:8042 --volume worker-data-2:/opt/hdfs_data/data --name worker-node-2 worker-node:341
-p 9865:9864
-p 8043:8042

# ELIMINAR HDFS DATA

despues

postgres

docker volume create pgdata_volume
docker network create hive-net
docker build -t postgres:metastore ./postgres_server/
docker run -d -p 5432:5432 --network hive-net --volume pgdata_volume:/var/lib/postgresql/data --name postgres_hms -e POSTGRES_PASSWORD=postgres postgres:metastore

metastore

docker build -t hive:metastore ./hive_metastore/
docker run -d --network hive-net --network hadoop-network -p 9083:9083 --name hive hive:metastore

me hace falta el 8042 de los servidores otros

## NOTAS

Revisar el uso de docker commit para la creacion de imagen con el metodo manual y lograr persistir los cambios.exi

```bash
docker commit <nombre_del_contenedor> <nuevo_nombre_de_imagen>
```

-p 9866:9866/ se usa para conecciones internas

#!/bin/bash

# Wait for workers

for host in worker-node-1 worker-node-2; do
while ! nc -z $host 9864; do
echo "Waiting for $host DataNode..."
sleep 5
done
done

# Start HDFS and YARN

start-dfs.sh
start-yarn.sh

/bin/bash

# Falta Crear volumenes en /opt/hadoop/data

# docker build -t hadoop-master:341 .

# Esperar a que los workers estén disponibles y copiar llaves SSH

for host in worker-node-1 worker-node-2; do
until sshpass -p 'hadoop' ssh -o StrictHostKeyChecking=no hadoop@$host "echo Conectado a $host"; do
    echo "Esperando a que $host esté disponible..."
    sleep 5
  done
  sshpass -p 'hadoop' ssh-copy-id -o StrictHostKeyChecking=no hadoop@$host
done
