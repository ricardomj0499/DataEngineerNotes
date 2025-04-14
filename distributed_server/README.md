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

