FROM pseudo:341

RUN sudo service ssh start && \
    sudo ssh-keygen -A && \
    mkdir -p /home/hadoop/hdfs/datanode && \
    chown -R hadoop:hadoopgrp /home/hadoop/hdfs/

COPY --chown=root:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/
# copy --chown=root:hadoopgrp ssh/conf  /home/hadoop/.ssh/


# COPY entrypoint.sh /entrypoint.sh

EXPOSE 22
EXPOSE 8020
ENTRYPOINT ["sudo","/usr/sbin/sshd","-D"]
