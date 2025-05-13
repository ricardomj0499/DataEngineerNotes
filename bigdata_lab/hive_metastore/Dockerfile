FROM ubuntu:24.04


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
    tar -xzf hive-standalone-metastore-3.0.0-bin.tar.gz --strip-components=1 --no-same-owner && \
    rm hive-standalone-metastore-3.0.0-bin.tar.gz && \
    chown -R root:hivegrp ${METASTORE_HOME} && \
    chmod -R 775 ${METASTORE_HOME}

EXPOSE 9083

USER hive

CMD ["/bin/bash"]
# docker build -t hive:metastore .\hive_metastore\