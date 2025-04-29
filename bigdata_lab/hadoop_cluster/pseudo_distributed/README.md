# README - Configuración de Hadoop en Modo Pseudo-Distribuido

Este documento describe los pasos para configurar un entorno **pseudo-distribuido** de Hadoop a partir de una imagen base.

---

## 1. Editar `hadoop-env.sh`

Ruta del archivo:

```bash
/etc/hadoop/hadoop-env.sh
```

Agregar o modificar las siguientes líneas para configurar Java:

```bash
# Set to the root of your Java installation
export JAVA_HOME=/usr/java/latest
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

---

## 2. Editar `core-site.xml`

Ruta del archivo:

```bash
/etc/hadoop/core-site.xml
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
/etc/hadoop/hdfs-site.xml
```

Agregar la siguiente configuración:

```xml
<property>
    <name>dfs.replication</name>
    <value>1</value>
</property>
```

---

## 4. Configurar SSH

En la carpeta `/home` del contenedor, generar las llaves SSH:

```bash
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```

Iniciar el servicio SSH:

```bash
$ sudo service ssh start
```

---

## 5. Inicializar HDFS

Formatear el `namenode`:

```bash
$ hdfs namenode -format
```

---

## 6. Iniciar HDFS

Levantar los servicios de Hadoop:

```bash
$ start-dfs.sh
```

---

## Nota Final

Una vez completados estos pasos dentro del contenedor, puedes **crear una nueva imagen** con estos cambios usando:

```bash
docker commit <nombre_del_contenedor> <nuevo_nombre_de_imagen>
```

Ejemplo:

```bash
docker commit hadoop-container hadoop-pseudo:v1
```

Así tendrás una imagen lista para usar Hadoop en modo pseudo-distribuido de manera inmediata.

docker run -it -p 9870:9870 -p 8088:8088 --name pseudo pseudo:341

A este punto tengo una imagen qe levanta los servicios de hdfs y yyarn

Me hace falta poder levatar y relevantar los contenedores con volumenes para persistencia d elos datos. No se nada de esto por lo que tengo que estudiar primero.
