#!/bin/bash
set -x
sudo service ssh start
# Ruta al directorio donde HDFS guarda la metadata del Namenode
HDFS_NAMENODE_DIR=/home/hadoop/hdfs/namenode

# Si no existe la metadata, formatear
if [ ! -f "$HDFS_NAMENODE_DIR/current/VERSION" ]; then
    echo "Formateando Namenode por primera vez..."
    hdfs namenode -format -force
else
    echo "Namenode ya formateado, saltando formato."
fi

sshpass -p 'hadoop' ssh-copy-id -o StrictHostKeyChecking=no hadoop@worker-node-1 
sshpass -p 'hadoop' ssh-copy-id -o StrictHostKeyChecking=no hadoop@worker-node-2 

start-dfs.sh
start-yarn.sh
tail -f /dev/null
