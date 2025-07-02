FROM pseudo:341

COPY --chown=hadoop:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/

RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \
    sshpass && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

# Crear directorio para el namenode
RUN mkdir -p /home/hadoop/hdfs/namenode && \
    chown -R hadoop:hadoopgrp /home/hadoop/hdfs

# Copiar el entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]