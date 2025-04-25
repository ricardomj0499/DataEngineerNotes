FROM hadoop:341

USER root
RUN service ssh restart

COPY etc/hadoop/core_site.xml $HADOOP_HOME/etc/hadoop/
COPY etc/hadoop/hdfs-site.xml $HADOOP_HOME/etc/hadoop/


# SSH setup (needed for Hadoop pseudo-distributed mode)
#RUN ssh-keygen -q -t rsa -P '' -f ~/.ssh/id_rsa -y && \
#cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
#chmod 0600 ~/.ssh/authorized_keys


CMD ["/bin/bash"]