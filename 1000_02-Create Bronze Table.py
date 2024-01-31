# Databricks notebook source
print("Step 2 - Bronze Table")

# COMMAND ----------

# MAGIC %run ./CreateWidgets

# COMMAND ----------

url = dbutils.widgets.getArgument('fileSourceURL')
saveFile = dbutils.widgets.getArgument('fileTargetPath')

# COMMAND ----------

jsonDF = spark.read.option("multiline","true").json( saveFile )
jsonDF.createOrReplaceTempView('json_data')

# COMMAND ----------

# MAGIC %sql
# MAGIC USE workflows.`1-bronze`;
# MAGIC CREATE OR REPLACE TABLE raw_population
# MAGIC AS SELECT * FROM json_data

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM raw_population
