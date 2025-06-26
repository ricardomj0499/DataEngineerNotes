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

docker run -d --cap-add=sys_nice -p 9870:9870 -p 8088:8088 -p 9000:9000 -p 8020:8020 --network hadoop-network --volume master-data:/opt/hdfs_data/data --name master-node master-node:341

docker run -d --cap-add=sys_nice --network hadoop-network --volume worker-data-1:/opt/hdfs_data/data --name worker-node-1 worker-node:341

docker run -d --cap-add=sys_nice --network hadoop-network --volume worker-data-2:/opt/hdfs_data/data --name worker-node-2 worker-node:341

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
