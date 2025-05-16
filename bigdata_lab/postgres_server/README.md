https://hub.docker.com/_/postgres/

docker volume create pgdata_volume

docker build -t postgres:metastore .\postgres_server\

docker run -d -p 5432:5432 --network hive-net --volume pgdata_volume:/var/lib/postgresql/data --name postgres_hms -e POSTGRES_PASSWORD=postgres postgres:metastore

I know it is not secure, but as it is for learnig, I might be come later to this to fix this
