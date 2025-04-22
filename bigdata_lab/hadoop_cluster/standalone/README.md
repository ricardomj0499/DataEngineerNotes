# 🐘 Apache Hadoop Base Image - Standalone Mode

Esta imagen Docker instala Apache Hadoop en modo **Standalone** (no distribuido, todo corre en el sistema de archivos local=file:///, no hay namenode ni datanode ni RM, corre como un solo proceso de Java), ideal como punto de partida para configuraciones más avanzadas (pseudo o full distributed). Usa `ubuntu:24.04` como base y Hadoop 3.4.1 por defecto.

## ¿Qué incluye?

- Java 11 (`openjdk-11-jre-headless`)
- Herramientas esenciales: `wget`, `ssh`, `pdsh`
- Descarga automática de Hadoop (`$HADOOP_VERSION`)
- Usuario `hadoop` listo para usar
- No modifica los archivos de configuración (`core-site.xml`, `hdfs-site.xml`, etc.)

## Cómo construir la imagen

Desde el directorio raíz del proyecto(DISTRIBUTED_SERVER):

```bash
docker build -t hadoop:341 -f ./hadoop/hadoop_base/Dockerfile ./hadoop/hadoop_base
```

Para usar otra versión de Hadoop:

```bash
docker build --build-arg HADOOP_VERSION=3.4.0 -t hadoop:340 ./hadoop/hadoop_base
```

## Ejecutar el contenedor

```bash
docker run -it --name hadoop_test hadoop:341
```

Esto te da una terminal interactiva como el usuario `hadoop`.

## Prueba rápida (modo local)

```bash
mkdir input
cp etc/hadoop/*.xml input
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar grep input output 'dfs[a-z.]+'
cat output/*
```

Este comando corre un job de ejemplo usando archivos de configuración como entrada. Preferiblemente cambiar al home del usuario con `cd` y despues cambiar las rutas agregando `$HADOOP_HOME` al principio de las mismas.

## Variables de entorno definidas

```
DEBIAN_FRONTEND=noninteractive
HADOOP_VERSION=3.4.1
HADOOP_HOME=/opt/hadoop
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
PATH=$PATH:/opt/hadoop/bin:/opt/hadoop/sbin
```

Puedes cambiar `HADOOP_VERSION` al momento del build con `--build-arg`.

## Directorio esperado de instalación

```
/opt/hadoop/
├── bin/
├── sbin/
├── etc/hadoop/
└── share/hadoop/
```

## Notas

- Esta imagen **no tiene configuraciones activas de HDFS ni YARN**.
- Ideal para pruebas locales o como base para clusters más grandes.

## Recursos útiles / Otras fuentes de descarga

- https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
- https://hadoop.apache.org/docs/r3.4.1/

## Otras fuentes de descarga

- https://archive.apache.org/dist/hadoop/common

- https://downloads.apache.org/hadoop/common

- https://dlcdn.apache.org/hadoop/common
