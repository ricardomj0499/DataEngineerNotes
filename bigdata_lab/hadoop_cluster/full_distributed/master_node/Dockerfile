FROM pseudo:341

COPY --chown=root:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/

USER root 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    sshpass && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh

EXPOSE 9870
EXPOSE 8088
EXPOSE 9000
EXPOSE 8020
EXPOSE 22

RUN sudo mkdir -p /home/hadoop/hdfs/namenode && \
    sudo chown -R hadoop:hadoopgrp /home/hadoop/hdfs
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER hadoop


#"" 
ENTRYPOINT ["/entrypoint.sh"] 

#  Falta Crear volumenes en /opt/hadoop/data
# docker build -t hadoop-master:341 .

