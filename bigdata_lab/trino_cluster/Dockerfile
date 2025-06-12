FROM ubuntu:24.04

# ---- Build arguments ----
ARG TRINO_VERSION=476

# ---- Environment variables ----
ENV DEBIAN_FRONTEND=noninteractive \
    TRINO_HOME=/opt/trino \
    JAVA_HOME=/usr/lib/jvm/temurin-24-jre-amd64

RUN echo "trino soft nofile 131072" >> archivo.txt  && \
    echo "trino hard nofile 131072" >> archivo.txt  && \
    echo "trino soft nproc 128000" >> archivo.txt  && \
    echo "trino hard nproc 128000" >> archivo.txt

# ---- Install Java, SSH, wget, pdsh ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-transport-https  \
    wget \gpg \
    ca-certificates && \
    wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null && \
    echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^UBUNTU_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list  && \
    apt-get update && \
    apt-get install -y --no-install-recommends temurin-24-jre && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ---- Prepare Trino directories and user ----
RUN groupadd -r trinogrp && \
    useradd -r -m -s /bin/bash -g trinogrp trino && \
    echo 'trino:trino' | chpasswd && \ 
    usermod -aG sudo trino && \
    echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir -p ${TRINO_HOME} && \
    mkdir -p ${TRINO_HOME}/data

WORKDIR ${TRINO_HOME}

# ---- Download and extract Trino ----
RUN wget -q https://repo1.maven.org/maven2/io/trino/trino-server/${TRINO_VERSION}/trino-server-${TRINO_VERSION}.tar.gz && \
    tar -xzf trino-server-${TRINO_VERSION}.tar.gz --no-same-owner && \
    rm trino-server-${TRINO_VERSION}.tar.gz && \
    chown -R root:trinogrp ${TRINO_HOME} && \
    chmod -R 775 ${TRINO_HOME}

USER trino

CMD ["/bin/bash"]
