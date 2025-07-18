#!/bin/bash
set -e
set -x

MODE=$1
MASTER_URL=${2:-spark://spark-master:7077}

case "$MODE" in
  master)
    echo "Starting Spark Master..."
    exec "$SPARK_HOME/bin/spark-class" org.apache.spark.deploy.master.Master \
      --host spark-master \
      --port 7077 \
      --webui-port 8080
    ;;
  worker)
    echo "Starting Spark Worker with master URL: $MASTER_URL"
    exec "$SPARK_HOME/bin/spark-class" org.apache.spark.deploy.worker.Worker "$MASTER_URL"
    ;;
  *)
    echo "Usage: $0 {master|worker} [master-url]"
    exit 1
    ;;
esac