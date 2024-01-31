# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text('fileSourceURL', 'https://raw.githubusercontent.com/JS-DevTools/static-mock-data/master/employees.json', 'URL to download from')
dbutils.widgets.text('fileTargetPath', "/Volumes/workflows/0-landing/downloads/sample.json", 'Path to save to')
