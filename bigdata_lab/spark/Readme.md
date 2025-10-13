docker build -t spark:4.0.0 .\spark\
docker run -it --network spark-network --network hadoop-network --network hive-net -p 8081:8080 spark:4.0.0
pyspark --conf spark.yarn.appMasterEnv.JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 --conf spark.executorEnv.JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 --conf spark.yarn.am.env.JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
df = spark.createDataFrame([[1,"Ricardo"]],["id","name"])
df.write.mode("overwrite").format("parquet").saveAsTable('test2')

spark.app.name (none) The name of your application. This will appear in the UI and in log data.

spark.driver.cores 1 Number of cores to use for the driver process, only in cluster mode.
