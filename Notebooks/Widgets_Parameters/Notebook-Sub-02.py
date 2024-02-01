# Databricks notebook source
print("When a notebook is invoked via the API, it runs in a separate session ✋🏼")

# COMMAND ----------

# This line would fail, since this child notebook does NOT run in the
# same session as the master and cannot see the widget created there
# print("Color => " + getArgument("color")) 

# COMMAND ----------

# These two lines work fine, these are paramters that were passed
print(dbutils.widgets.getArgument("p1"))
print(getArgument("p2"))

# COMMAND ----------

dbutils.notebook.exit("This is the value returned")
