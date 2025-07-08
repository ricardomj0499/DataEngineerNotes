FROM hadoop:341



COPY --chown=root:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/

# SSH setup (needed for Hadoop pseudo-distributed mode)
#RUN ssh-keygen -q -t rsa -P '' -f ~/.ssh/id_rsa && \
#cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
#chmod 0600 ~/.ssh/authorized_keys

#COPY entrypoint.sh /entrypoint.sh

USER root

RUN useradd -m -s /bin/bash -g hadoopgrp ricardo

USER ricardo

#ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/bin/bash"]

# anadir a hadoopgrp