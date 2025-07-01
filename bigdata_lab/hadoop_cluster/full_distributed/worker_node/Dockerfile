FROM pseudo:341

# ---- Install Java 21 for Spark ----
RUN sudo apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN sudo service ssh start && \
    sudo ssh-keygen -A && \
    mkdir -p /home/hadoop/hdfs/datanode && \
    chown -R hadoop:hadoopgrp /home/hadoop/hdfs/

COPY --chown=root:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/


ENTRYPOINT ["sudo","/usr/sbin/sshd","-D"]
