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
RUN wget -q https://dlcdn.apache.org/spark/spark-4.0.0/spark-4.0.0-bin-hadoop3.tgz && \
    tar -xzf spark-4.0.0-bin-hadoop3.tgz --strip-components=1 --no-same-owner && \
    rm spark-4.0.0-bin-hadoop3.tgz && \
    chown -R root:sparkgrp ${SPARK_HOME} && \
    chmod -R 775 ${SPARK_HOME}


# ---- Install Java, SSH, wget, pdsh ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 9870
# ---- Prepare Hadoop directories and user ----
RUN groupadd -r hadoopgrp && \
    usermod -aG hadoopgrp spark && \
    echo "%sudo   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER spark

COPY --chown=spark:hadoopgrp etc/hadoop/* $SPARK_HOME/etc/hadoop/
COPY --chown=hadoop:sparkgrp conf/* $SPARK_HOME/conf

CMD ["/bin/bash"]
# df = spark.read.text('/user/hadoop/test_file_1.csv')
# 
# pyspark --master yarn --conf spark.yarn.appMasterEnv.JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 --conf spark.executorEnv.JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 --conf spark.yarn.am.env.JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
# 15002. port

#textFile.select(sf.size(sf.split(textFile.value, "\s+")).name("numWords")).agg(sf.max(sf.col("numWords"))).collect()

#wordCounts = textFile.select(sf.explode(sf.split(textFile.value, "\s+")).alias("word")).groupBy("word").count()

#spark-submit --master "local[4]" SimpleApp.py