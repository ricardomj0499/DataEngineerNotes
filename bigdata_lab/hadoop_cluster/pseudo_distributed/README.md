# Configuración de Hadoop en Modo Pseudo-Distribuido

Este documento describe los pasos para configurar un entorno **pseudo-distribuido** de Hadoop a partir de una imagen base.
Aca está definido como armarlo manualmente, al final del documento vienen los comandos para iniciar un contenedor listo para pseudo distributed.

En caso de tener la imagen hadoop:341 construida, correr:

```bash
docker run -it -p 9870:9870 -p 8088:8088 -p 9864:9864 -p 8042:8042 --name pseudo-distributed pseudo:341
```

O bien:

```bash
docker compose up -d
```

Dentro de la carpeta de pseudo-distributed

---

## 1. Editar `hadoop-env.sh`

Ruta del archivo:

```bash
$HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

Agregar o modificar las siguientes líneas para configurar Java:

```bash
# Set to the root of your Java installation
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

---

## 2. Editar `core-site.xml`

Ruta del archivo:

```bash
$HADOOP_HOME/etc/hadoop/core-site.xml
```

Agregar la siguiente configuración:

```xml
<property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
</property>
```

---

## 3. Editar `hdfs-site.xml`

Ruta del archivo:

```bash
$HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

Agregar la siguiente configuración:

```xml
<property>
    <name>dfs.replication</name>
    <value>1</value>
</property>
```

## 4. Editar `yarn-site.xml`

Ruta del archivo:

```bash
$HADOOP_HOME/etc/hadoop/yarn-site.xml
```

Agregar la siguiente configuración:

```xml
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
    </property>
```

---

## 5. Configurar SSH

En la carpeta `/home` del contenedor, generar las llaves SSH:

```bash
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```

---

## 6. Inicializar HDFS

Formatear el `namenode`:

```bash
$ hdfs namenode -format
```

---

## 7. Revisar UIs de HDFS y YARN

Acceder a localhost:9870 y localhost:8088

---

## 8. Creacion mediante docker build

Esto fueron los pasos para levantar los servicios manualmente desde la imagen hadoop:341, para hacerlo mediante una imagen correr:

```bash
docker build -t pseudo:341 .\hadoop_cluster\pseudo_distributed\
```

```bash
docker run -it -p 9870:9870 -p 8088:8088 -p 9864:9864 -p 8042:8042 --name pseudo-distributed pseudo:341
```

Para levantar el sistema en modo interactivo una vez fue apagado la primera vez

```bash
docker start -ai pseudo
```

# Notas

Acá Hace falta incluir el volumen para persistencia de datos, así como varias configuraciones especialmente de los directorios de los datos. Estas configuraciones no serán agregadas en este momento, ya que serán estudiadas más adelante en el clúster full distribuido. Revisar la documentación o los archivos del full_distributed para saber como configurar los archivos mencionados.

Si se explora la web, se accede mediante localhost:puerto
