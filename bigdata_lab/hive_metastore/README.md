---
# 🐝 Hive Standalone Metastore en Docker

Este proyecto contiene una imagen Docker personalizada para levantar un **Hive Standalone Metastore** (v3.0.0) sobre una base de datos PostgreSQL. Ideal para entornos de desarrollo y pruebas locales, especialmente en arquitecturas tipo data lake.
---

## 📚 Recursos Relevantes

- [Documentación oficial de Hive](https://hive.apache.org/docs/latest/)
- [Configuración de Hive Metastore](https://hive.apache.org/docs/latest/adminmanual-metastore-3-0-administration_75978150/)
- [Descarga de Hive Standalone Metastore 3.0.0](https://dlcdn.apache.org/hive/hive-standalone-metastore-3.0.0/)
- [Thrift IDL para Hive](https://thrift.apache.org/docs/idl)
- [Autorización basada en almacenamiento](https://hive.apache.org/docs/latest/storage-based-authorization-in-the-metastore-server_45876440/)

---

## 🏗️ Requisitos

- Docker
- Una red Docker (`hive-net`)
- PostgreSQL configurado como backend (puede usar la imagen [`postgres:metastore`](#postgres-metastore))

---

## 📁 Estructura del Proyecto

```
.
├── hive_metastore/
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── conf/
│   │   └── metastore-site.xml
│   └── hadoop_conf/
│       └── core-site.xml
```

---

## 🧱 Build de la Imagen

```bash
docker build -t hive:metastore ./hive_metastore/
```

---

## ▶️ Ejecución del Contenedor

```bash
docker run -d --network hive-net --network hadoop-network -p 9083:9083 --name hive hive:metastore
```

> 📌 _Nota:_ Asegúrate de que el contenedor de PostgreSQL esté levantado antes de iniciar este servicio, ya que se conecta a `postgres_hms` en la red `hive-net`.

---

## 🔐 Conexión con PostgreSQL

El `metastore-site.xml` define los siguientes parámetros de conexión:

```xml
<name>javax.jdo.option.ConnectionURL</name>
<value>jdbc:postgresql://postgres-hms:5432/metastore</value>

<name>javax.jdo.option.ConnectionUserName</name>
<value>hive</value>

<name>javax.jdo.option.ConnectionPassword</name>
<value>hive</value>
```

> ⚠️ Seguridad: Estas credenciales son públicas y deben ser cambiadas para ambientes reales. Considera usar Docker secrets o inyección de variables en producción.

---

## 🚀 ¿Qué hace el `entrypoint.sh`?

1. Verifica si el esquema del metastore ya está inicializado.
2. Si no lo está, ejecuta `schematool -initSchema` para crearlo.
3. Lanza el proceso `start-metastore`.

> Puedes modificarlo para agregar lógica de espera a PostgreSQL o validaciones adicionales si lo deseas.

---

## ⚙️ Configuración de HDFS (opcional)

`core-site.xml` está preconfigurado para usar un sistema de archivos HDFS en modo pseudo distribuido:

```xml
<name>fs.defaultFS</name>
<value>hdfs://pseudo-distributed:9000</value>
```

Asegúrate de levantar un contenedor o clúster con HDFS que se registre con ese nombre en la red `hive-net`. Si el contenedor de hdfs esta en otra read, asegurate de incluir a este contenedor en esa red mediante `docker network connect hive-net other_net`

---

## 🧪 Verificación

Puedes probar que el Metastore esté activo en el puerto `9083` o conectarte desde un cliente que use Thrift, como Hive CLI, Spark o Presto.

---

## 🔄 Integración con otros servicios

Para completar un entorno de laboratorio, puedes levantar en la misma red:

- PostgreSQL (`postgres:metastore`)
- HDFS (`namenode`, `datanode`)
- Hive CLI o Beeline
- Spark (`spark-shell`, `pyspark`, etc.)

---
