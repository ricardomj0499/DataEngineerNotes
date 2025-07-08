FROM pseudo:341

RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

COPY --chown=hadoop:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/

# Crear directorio para el namenode
RUN mkdir -p /opt/hadoop/data && \
    chown -R hadoop:hadoopgrp /opt/hadoop/data

# Copiar el entrypoint
COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]