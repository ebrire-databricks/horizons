# Databricks notebook source
print("Step 1")

# COMMAND ----------

df = spark.sql( """select * from samples.nyctaxi.trips""")
display(df)
