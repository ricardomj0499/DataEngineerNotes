FROM ubuntu:24.04


# ---- Environment variables ----
ENV DEBIAN_FRONTEND=noninteractive \
    SPARK_HOME=/opt/spark \
    JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 \
    PYTHON=/usr/bin/python3 \
    PATH=$PATH:$PYTHON:/opt/spark/bin:/opt/spark/sbin

# ---- Install Java, SSH, wget, pdsh ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \
    python3.12 \
    python3.12-venv \
    python3-pip \
    wget \
    ssh \
    pdsh \
    nano \
    sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Set default python and python3 to the new version
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1



# ---- Prepare Spark directories and user ----
RUN groupadd -r sparkgrp && \
    useradd -r -m -s /bin/bash -g sparkgrp spark && \
    echo 'spark:spark' | chpasswd && \ 
    usermod -aG sudo spark && \
    echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir -p ${SPARK_HOME}

WORKDIR ${SPARK_HOME}

# Instala dependencias de Python para PySpark
RUN python -m pip install --no-cache-dir --break-system-packages \
    pandas \
    pyarrow \
    numpy \
    grpcio \
    grpcio-status \
    pyspark

# ---- Download and extract Spark ----
RUN wget -q https://dlcdn.apache.org/spark/spark-4.0.0/spark-4.0.0-bin-hadoop3-connect.tgz && \
    tar -xzf spark-4.0.0-bin-hadoop3-connect.tgz --strip-components=1 --no-same-owner && \
    rm spark-4.0.0-bin-hadoop3-connect.tgz && \
    chown -R root:sparkgrp ${SPARK_HOME} && \
    chmod -R 775 ${SPARK_HOME}

COPY --chown=root:sparkgrp etc/hadoop/* $SPARK_HOME/etc/hadoop/
COPY --chown=root:sparkgrp conf/* $SPARK_HOME/conf

# ---- Install Java, SSH, wget, pdsh ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 9870

USER spark

CMD ["/bin/bash"]
# df = spark.read.text('/user/hadoop/test_file_1.csv')
# pyspark --master yarn
# 15002. port