FROM hadoop:341

COPY --chown=root:hadoopgrp etc/hadoop/* $HADOOP_HOME/etc/hadoop/

# SSH setup (needed for Hadoop pseudo-distributed mode)
RUN mkdir -p ~/.ssh && \
    ssh-keygen -q -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

COPY entrypoint.sh /entrypoint.sh

EXPOSE  9870 8088 9864 8042

ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/bin/bash"]
