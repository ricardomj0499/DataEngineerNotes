#!/bin/bash
set -e

# Iniciar SSH
sudo service ssh start

# Formatear el Namenode si es la primera vez
HDFS_NAMENODE_DIR=/home/hadoop/hdfs/namenode

if [ ! -f "$HDFS_NAMENODE_DIR/current/VERSION" ]; then
    echo "Formateando Namenode por primera vez..."
    hdfs namenode -format -force -nonInteractive
else
    echo "Namenode ya formateado, saltando formato."
fi

# Iniciar HDFS
start-dfs.sh

# Iniciar YARN
start-yarn.sh

# Mantener el contenedor corriendo
tail -f /dev/null