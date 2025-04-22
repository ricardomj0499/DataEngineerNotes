Ideas principales
hadoop base por ahora es para un server stanadlone, que mas adelante sera pseudo-distributed

https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation

ver ccual es la diferencia entre hadoop pseudo distribitud y full distribuido
la configurtacion para el pseudo distributed se va a realizar desde otro docker file
este solo tiene la conf inicial de hadoop para no tener que estar descargando todos los archivos dede cero

al crear un contenedor y al tratar de acceder a hadoop
dice que root no tiene acceso, no esta poniendo las variables en el bash de root

lo que quiero crear es una imagen de hadooop base sin nada configurado
para un server standalone, con un usuario hadoop listo para usarr

docker build -t hadoop:341 -f ./hadoop/hadoop_base/Dockerfile ./hadoop/hadoop_base
docker run -ia --name hadoop_test hadoop:341

# https://archive.apache.org/dist/hadoop/common/hadoop-3.4.1/

# https://downloads.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz

# https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz

run
docker build --build-arg HADOOP_VERSION=3.4.0 .
