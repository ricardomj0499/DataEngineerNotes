docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker run -d -p 5432:5432 --network hive-net --name postgres_hms -e POSTGRES_PASSWORD=postgres postgres:metastore
docker build -t postgres:metastore .\postgres_server\
