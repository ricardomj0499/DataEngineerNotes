# 🐘 Big Data Cluster con Hadoop, HDFS, YARN, Trino, Hive, Delta Lake y Kafka, etc...

Este proyecto nace de la idea de crear un **cluster** de Big data con el objetivo de experimentar con **Docker** y simular una ambiente con sus diferentes servidores y tecnlogias. Empezando por Hadoop y expandiéndose progresivamente con otras herramientas como **Trino**, **Hive Metastore**, **Delta Lake** y **Kafka**, entre otras tecnologias que me llamen la atencion conforme avance en la configuracion y la creacion del proyecto. Debido a mi falta de expericiencia con docker y viendo que es una tecnologia muy usada en el ambiente labora, está pensado para aprender profundamente cómo funciona cada componente, incluyendo **configuración manual, autenticación, usuarios y red entre nodos**, ya que tratare de no usar imagenes pre creadas si no hacer todo desde cero. Tengo experiencia en la configuracion de servidores locales/on-premises, asi como las diferentes tecnlogias aca mencionadas, pero debido a la naturaleza de mi actual trabajo y sus politicas no he podido experimentar con el uso de docker.

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

- Aprender a instalar Hadoop **desde cero**
- Controlar la red y los puertos entre contenedores
- Simular un entorno de producción con **SSH y múltiples nodos**
- Conectarte desde una máquina externa (cliente WSL2)
- Enfrentar problemas reales como **autenticación**, **usuarios**, **conexiones distribuidas**, etc.

---

## 📦 Estructura del proyecto

--

## NOTA

Road Map inicial del proyecto.

- Servidor inicial hadoop Standalone(Con usuario listo para crear un pseudo-distribuido ya sea mediante un contenedor inmediado o la creacion de una imagen nueva en base a este)
- Servidor Hadoop Pseudo Distruido
- Servidor postgres (posiblemente este si lo use con una imagen lista para el uso) (servira tanto para probar conexion futura de trino como para el hive - metastore)
- Spark (posiblemente en el ambiente pseudo distribuido de Hadoop)
- Hive metastore
- Maquina cliente capaz de lanzar jobs usando spark y usando hadoop como motor de computo y guardado en el hdfs. Pero no realiza procesamiento. (Guardar datos en delta o hudo o iceberg)
- trino
- Expandir con el uso de kafka, flink, unity catalog, nessie o alguna otra herramiento interesante que encuentre, puede incluir herramientas de data governance y lineage.
- En algun punto incluir docker compose, por ahora, trabajo con Build y runs directas.
- Asi como incluir el uso de volumenes
- Por ultimo expandir el servidor de hadoop a full distribuido
- Tema aparte, despues de esto, investigar soluciones en la nube como bdt, databricks, etc, asi como darle una repasada a warehouses, sql analysis services y demas bases de la ingeniera de datos
