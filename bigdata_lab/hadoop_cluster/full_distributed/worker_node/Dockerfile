FROM pseudo:341

# ---- Install Java 21 for Spark ----
RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

RUN sudo service ssh start && \
    sudo ssh-keygen -A && \
    mkdir -p /home/hadoop/hdfs/datanode && \
    chown -R hadoop:hadoopgrp /home/hadoop/hdfs/

COPY --chown=hadoop:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/

EXPOSE  9870 8088 9864 8042

ENTRYPOINT ["sudo","/usr/sbin/sshd","-D"]
