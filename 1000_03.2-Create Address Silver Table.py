# Databricks notebook source
print("Step 3 - Silver Tables")

# COMMAND ----------

# MAGIC %sql
# MAGIC USE workflows.`1-bronze`;
# MAGIC SELECT * FROM raw_population

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE workflows.`2-silver`.addresses
# MAGIC AS
# MAGIC SELECT ssn, 
# MAGIC        address.street as street,
# MAGIC        address.city as city,
# MAGIC        address.state as state,
# MAGIC        address.zip as zip
# MAGIC FROM raw_population;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workflows.`2-silver`.addresses
