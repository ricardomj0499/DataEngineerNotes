crete net

docker network create trino-net

cd trino-server-476/

bin/launcher run
docker build -t trino:476 .\trino_cluster\

docker build -t trino-master:476 .\trino_cluster\trino_master\
docker run -d --name trino-master -p 8080:8080 --network trino-net --network hive-net trino-master:476

docker build -t trino-worker:476 .\trino_cluster\trino_worker\
docker run -d --name trino-worker --network trino-net trino-worker:476
