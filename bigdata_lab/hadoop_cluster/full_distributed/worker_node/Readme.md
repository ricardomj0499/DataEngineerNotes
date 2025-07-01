# Hadoop Worker Node - Notas sobre la Construcción y Funcionamiento de la Imagen

## 🛠️ 1. Gestión de Procesos en el Contenedor

En esta imagen **no se inician automáticamente los servicios de Hadoop (DataNode o NodeManager)**.

- Los servicios son inicializados desde el nodo master utilizando los comandos:

```bash
start-dfs.sh
start-yarn.sh
```

- Este enfoque simula un entorno real donde existe un servidor maestro que controla el inicio de servicios en los workers.

### ⚠️ Implicación:

- Es necesario que el contenedor tenga un proceso principal corriendo para que Docker lo mantenga activo.
- Para esto, actualmente se utiliza:

```dockerfile
ENTRYPOINT ["sudo", "/usr/sbin/sshd", "-D"]
```

Esto mantiene el contenedor vivo ejecutando el servidor SSH en primer plano.

### 🚫 Problema de este enfoque:

- Se rompe parcialmente la filosofía de Docker de tener **un único proceso principal**.
- Cuando se inician los servicios de Hadoop (`datanode` y `nodemanager`), estos corren como procesos adicionales dentro del mismo contenedor.
- Si Docker reinicia el contenedor, **los servicios de Hadoop no se reinician automáticamente**, ya que no forman parte del `ENTRYPOINT`.

### ✔️ Solución propuesta (mejor práctica):

- Crear un `entrypoint.sh` que arranque tanto el servidor SSH como los daemons de Hadoop.

Ejemplo de `entrypoint.sh`:

```bash
#!/bin/bash
set -e

# Iniciar servidor SSH
sudo service ssh start

# Iniciar DataNode
echo "Starting DataNode..."
hdfs --daemon start datanode

# Iniciar NodeManager
echo "Starting NodeManager..."
yarn --daemon start nodemanager

# Mantener el contenedor en ejecución
tail -f /dev/null
```

---

## ☕ 2. Instalación de Java

- En esta imagen se instala **Java 21** debido a que se planea utilizar Spark dentro del clúster.
- Spark requiere versiones más modernas de Java (17 o superior en versiones recientes).

## 🔐 3. Configuración del Servidor SSH

Durante la construcción de la imagen se ejecuta:

```dockerfile
RUN sudo service ssh start && sudo ssh-keygen -A
```

### 🤔 ¿Por qué se hace esto?

- En pruebas realizadas, se detectó que utilizar solamente:

```bash
ssh-keygen -A
```

**no era suficiente**, ya que algunas carpetas necesarias para el funcionamiento de `sshd` (como `/run/sshd`) **no eran creadas automáticamente**.

### ✔️ Soluciones alternativas válidas:

- Crear manualmente la carpeta requerida:

```dockerfile
RUN mkdir -p /run/sshd
```

- Luego ejecutar solo:

```bash
ssh-keygen -A
```

- Finalmente, iniciar el servicio SSH dentro del `entrypoint.sh` con:

```bash
sudo service ssh start
```

Esta es una forma más limpia y alineada con buenas prácticas en Docker.

---

## ✅ Resumen de Buenas Prácticas Propuestas

| Tema                 | Práctica Actual                               | Mejor Práctica Recomendada                                                                                      |
| -------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Proceso Principal    | SSH como ENTRYPOINT                           | entrypoint.sh que inicia SSH + Hadoop daemons                                                                   |
| Gestión de Servicios | Desde master con start-dfs.sh y start-yarn.sh | Válido, pero mejor si workers también inician solos                                                             |
| Instalación de Java  | Java 21                                       | ✅ Correcto por compatibilidad con Spark                                                                        |
| Configuración de SSH | ssh start en build                            | Crear /run/sshd + ssh-keygen -A en build(Aunque tengo entendido, que lo mejor es no usar ssh en estos amgiente) |

---

## 📜 Ejemplo Completo de entrypoint.sh

```bash
#!/bin/bash
set -e

# Start SSH service
sudo service ssh start

# Start Hadoop DataNode
echo "Starting DataNode..."
hdfs --daemon start datanode

# Start Hadoop NodeManager
echo "Starting NodeManager..."
yarn --daemon start nodemanager

# Keep container running
tail -f /dev/null
```

---

## 🚀 Consideraciones Finales

Este diseño busca balancear el aprendizaje sobre cómo funciona un clúster Hadoop real, incluyendo su interacción vía SSH, junto con la flexibilidad de un entorno Dockerizado.

Si el objetivo evoluciona hacia mayor automatización o integración con orquestadores como Kubernetes, se puede modificar la arquitectura eliminando SSH como dependencia y delegando el arranque de servicios a mecanismos de inicialización más modernos.
