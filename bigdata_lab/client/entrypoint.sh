#!/bin/bash
set -x
sudo service ssh start
# Ruta al directorio donde HDFS guarda la metadata del Namenode
HDFS_NAMENODE_DIR=/tmp/hadoop-hadoop/dfs/name

# Si no existe la metadata, formatear
if [ ! -f "$HDFS_NAMENODE_DIR/current/VERSION" ]; then
    echo "Formateando Namenode por primera vez..."
    hdfs namenode -format -force
else
    echo "Namenode ya formateado, saltando formato."
fi

start-dfs.sh
start-yarn.sh

/bin/bash 