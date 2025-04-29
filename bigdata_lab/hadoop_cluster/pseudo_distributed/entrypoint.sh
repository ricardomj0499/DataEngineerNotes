#!/bin/bash
set -e

# Ruta al directorio donde HDFS guarda la metadata del Namenode
#HDFS_NAMENODE_DIR=/opt/hadoop_tmp/hdfs/namenode

# Si no existe la metadata, formatear
#if [ ! -d "$HDFS_NAMENODE_DIR/current" ]; then
    #echo "Formateando Namenode por primera vez..."
    #hdfs namenode -format -force
#else
    #echo "Namenode ya formateado, saltando formato."
#fi

sudo service ssh start
hdfs namenode -format
start-dfs.sh
start-yarn.sh

/bin/bash 