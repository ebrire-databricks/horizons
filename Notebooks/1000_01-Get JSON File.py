# Databricks notebook source
print("Step 1 - Get Data")

# COMMAND ----------

# MAGIC %run ./CreateWidgets

# COMMAND ----------

dbutils.fs.ls('file:/Workspace/Repos/Workflows/horizons/Data')

# COMMAND ----------

url = dbutils.widgets.getArgument('fileSourceURL')
saveFile = dbutils.widgets.getArgument('fileTargetPath')
print("Parameters ==>", url, saveFile)

dbutils.fs.cp(url, saveFile)

# COMMAND ----------

dbutils.fs.ls(saveFile)
dbutils.fs.head(saveFile, 1024)

# COMMAND ----------

jsonDF = spark.read.option("multiline","true").json( saveFile )
display(jsonDF)
