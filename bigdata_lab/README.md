# 🐘 Big Data Cluster con Hadoop, HDFS, YARN, Trino, Hive, Delta Lake y Kafka

Este proyecto te permite construir un **clúster Big Data completo** desde cero usando **Docker**, empezando por Hadoop y expandiéndose progresivamente con otras herramientas como **Trino**, **Hive Metastore**, **Delta Lake** y **Kafka**. Está pensado para aprender profundamente cómo funciona cada componente, incluyendo **configuración manual, autenticación, usuarios y red entre nodos**.

---

## 🛠 Tecnologías involucradas

- [x] Hadoop 3.x (HDFS + YARN)
- [ ] Trino (SQL engine)
- [ ] Hive Metastore
- [ ] Delta Lake (con soporte Parquet)
- [ ] Apache Kafka
- [ ] Cliente externo (WSL2 o cualquier máquina externa)
- [ ] Autenticación y gestión de usuarios (Kerberos, LDAP, o personalizada)

---

## 🚀 Objetivo

> Crear un clúster donde cada componente se instale y configure manualmente dentro de contenedores, permitiendo:

- Aprender a instalar Hadoop y amigos **desde cero**
- Controlar la red y los puertos entre contenedores
- Simular un entorno de producción con **SSH y múltiples nodos**
- Conectarte desde una máquina externa (cliente WSL2)
- Enfrentar problemas reales como **autenticación**, **usuarios**, **conexiones distribuidas**, etc.

---

## 📦 Estructura del proyecto

docker build -t hadoop:master -f ./hadoop/dockerfile_master/Dockerfile ./hadoop/dockerfile_master
docker run -it --name hadoop_master hadoop:master /bin/bash
docker rm hadoop_master

--

En el hadoop base solo un stan alone (poder correo los ejemplos de la pagina stan adlone)

despues pseudo distributed (poder accceder a la pagina de hdfs y yarn - subir archivos manuales hdfs y ver las paginas y los servicios)

server con spark instalado (realizar hobs locales y)

spark en el cluster de hadoop para distributed

despues metastore para guardar datos no solo en memoria
