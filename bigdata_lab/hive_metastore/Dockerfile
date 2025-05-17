FROM hadoop:341

USER root

# ---- Environment variables ----
ENV DEBIAN_FRONTEND=noninteractive \
    METASTORE_HOME=/opt/hive \
    PATH=$PATH:/opt/hive/bin

# ---- Install Java, SSH, wget, pdsh ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    nano \
    ca-certificates \
    sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ---- Prepare Hive directories and user ----
RUN groupadd -r hivegrp && \
    useradd -r -m -s /bin/bash -g hivegrp hive && \
    usermod -aG sudo hive && \
    echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir -p ${METASTORE_HOME}

WORKDIR ${METASTORE_HOME}

# ---- Download and extract Hive ----
RUN wget -q https://dlcdn.apache.org/hive/hive-standalone-metastore-3.0.0/hive-standalone-metastore-3.0.0-bin.tar.gz && \
    wget https://jdbc.postgresql.org/download/postgresql-42.7.5.jar  && \
    tar -xzf hive-standalone-metastore-3.0.0-bin.tar.gz --strip-components=1 --no-same-owner && \
    rm hive-standalone-metastore-3.0.0-bin.tar.gz && \
    mv postgresql-42.7.5.jar lib/ && \
    chown -R root:hivegrp ${METASTORE_HOME} && \
    chmod -R 775 ${METASTORE_HOME}


COPY conf/metastore-site.xml ${METASTORE_HOME}/conf/
COPY hadoop_conf/core-site.xml ${HADOOP_HOME}/etc/hadoop/
COPY entrypoint.sh /entrypoint.sh


EXPOSE 9083

USER Hive

ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/bin/bash"]
