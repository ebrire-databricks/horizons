# Databricks notebook source
print("Step 1 - Download File")

# COMMAND ----------

# MAGIC %run ./CreateWidgets

# COMMAND ----------

url = dbutils.widgets.getArgument('fileSourceURL')
saveFile = dbutils.widgets.getArgument('fileTargetPath')

from urllib.request import urlretrieve
urlretrieve(url, saveFile)

# COMMAND ----------

dbutils.fs.ls(saveFile)
dbutils.fs.head(saveFile, 1024)

# COMMAND ----------

jsonDF = spark.read.option("multiline","true").json( saveFile )
display(jsonDF)
