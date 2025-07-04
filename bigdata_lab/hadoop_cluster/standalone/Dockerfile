FROM ubuntu:24.04

# ---- Build arguments ----
ARG HADOOP_VERSION=3.4.1

# ---- Environment variables ----
ENV DEBIAN_FRONTEND=noninteractive \
    HADOOP_VERSION=${HADOOP_VERSION} \
    HADOOP_HOME=/opt/hadoop \
    JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 \
    PATH=$PATH:/opt/hadoop/bin:/opt/hadoop/sbin

# ---- Install Java, SSH, wget, pdsh ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \
    wget \
    ssh \
    pdsh \
    nano \
    sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ---- Prepare Hadoop directories and user ----
RUN groupadd -r hadoopgrp && \
    useradd -r -m -s /bin/bash -g hadoopgrp hadoop && \
    echo 'hadoop:hadoop' | chpasswd && \ 
    usermod -aG sudo hadoop && \
    echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir -p ${HADOOP_HOME}

WORKDIR ${HADOOP_HOME}

# ---- Download and extract Hadoop ----
RUN wget -q https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz --strip-components=1 --no-same-owner && \
    rm hadoop-${HADOOP_VERSION}.tar.gz && \
    chown -R root:hadoopgrp ${HADOOP_HOME} && \
    chmod -R 775 ${HADOOP_HOME}

USER hadoop

CMD ["/bin/bash"]
