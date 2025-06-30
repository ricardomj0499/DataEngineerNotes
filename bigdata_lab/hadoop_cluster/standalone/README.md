# 🐘 Apache Hadoop Base Image - Standalone Mode

Esta imagen Docker instala Apache Hadoop en modo **Standalone** (no distribuido, todo corre en el sistema de archivos local=file:///, es como decir: fs.defaultFS=file:///; no hay namenode ni datanode ni RM, corre como un solo proceso de Java), ideal como punto de partida para configuraciones más avanzadas (pseudo o full distributed). Usa `ubuntu:24.04` como base y Hadoop 3.4.1 por defecto.

## ¿Qué incluye?

- Java 11 (`openjdk-11-jre-headless`)
- Herramientas esenciales: `wget`, `ssh`, `pdsh`, `nano` y `sudo`
- Versión de hadoop como ARG (`$HADOOP_VERSION`)
- Usuario `hadoop` listo para usar con sudo
- No modifica los archivos de configuración (`core-site.xml`, `hdfs-site.xml`, etc.)

## Cómo construir la imagen

Desde el directorio raíz del proyecto(BIGDATA_LAB):

```bash
docker build -t hadoop:341 ./hadoop_cluster/standalone
```

Para usar otra versión de Hadoop:

```bash
docker build --build-arg HADOOP_VERSION=3.4.0 -t hadoop:340 ./hadoop_cluster/standalone
```

## Ejecutar el contenedor

```bash
docker run -it --name hadoop-test hadoop:341
```

Esto te da una terminal interactiva como el usuario `hadoop`. Y ya que no tiene servicios corriendo, no tiene sentido iniciarlo en modo detached -d por lo que usamos -it para tener una sesión interactiva.

En caso de cerrar el contenedor y querer volver a ejecutarlo, podemos iniciarlo de alguna de las siguientes maneras. Ya que el docker dan da error ya que el contener ya existe.

```bash
docker start -ai hadoop-test
```

start: Inicia un contenedor detenido.

-a: Adjunta la salida (stdout/stderr) del contenedor al terminal.

-i: Permite interactuar con la entrada (stdin), útil si el contenedor es interactivo.

Si solo quieres levantarlo sin interactuar:

```bash
docker start hadoop-test
```

Si el contenedor ya está corriendo y quieres entrar a él:

```bash
docker exec -it hadoop-test bash
```

## Prueba rápida (modo local)

```bash
mkdir input
cp etc/hadoop/*.xml input
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar grep input output 'dfs[a-z.]+'
cat output/*
```

Este comando corre un job de ejemplo usando archivos de configuración como entrada, nos debe de dar `1       dfsadmin` el último comando . Preferiblemente, cambiar al home del usuario con `cd` y después cambiar las rutas agregando `$HADOOP_HOME` al principio de las mismas.

## Variables de entorno definidas

```
DEBIAN_FRONTEND=noninteractive
HADOOP_VERSION=3.4.1
HADOOP_HOME=/opt/hadoop
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
PATH=$PATH:/opt/hadoop/bin:/opt/hadoop/sbin:$JAVA_HOME/bin
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

## Recursos útiles / Otras fuentes de descarga

- https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
- https://hadoop.apache.org/docs/r3.4.1/

## Otras fuentes de descarga

- https://archive.apache.org/dist/hadoop/common

- https://downloads.apache.org/hadoop/common

- https://dlcdn.apache.org/hadoop/common

## Notas

- Esta imagen **no tiene configuraciones activas de HDFS ni YARN**.
- Ideal para pruebas locales o como base para clusters más grandes.
- Hace falta optimización en la imagen (por ejemplo, eliminar la carpeta share para eliminar archivos no necesarios).
- Uno de mis objetivos es, partir de esta imagen, lograr tener un pseudo distribuido, lo cual se puede lograr mediante comando, o haciendo otra imagen a partir de esta y dejando listo el pseudo distribuido (hecho en la carpeta pseudo_distributed).
- Soy consciente de que se podría realizar de mejor manera, pero el objetivo era armar un server sencillo y jugar con docker.
