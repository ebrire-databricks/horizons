# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

#url = 'https://raw.githubusercontent.com/JS-DevTools/static-mock-data/master/employees.json'
dbutils.widgets.text('fileSourceURL', 'file:/Workspace/Repos/Workflows/horizons/Data/persons.json', 'Location to download from')
dbutils.widgets.text('fileTargetPath', "/Volumes/workflows/0-landing/downloads/sample.json", 'Path to save to')
