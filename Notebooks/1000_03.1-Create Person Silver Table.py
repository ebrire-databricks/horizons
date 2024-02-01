# Databricks notebook source
print("Step 3 - Silver Tables")

# COMMAND ----------

# MAGIC %sql
# MAGIC USE workflows.`1-bronze`;
# MAGIC SELECT * FROM raw_population

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE workflows.`2-silver`.persons
# MAGIC AS
# MAGIC SELECT ssn, 
# MAGIC        name.first as FirstName,
# MAGIC        name.last as LastName,
# MAGIC        department,
# MAGIC        dob,
# MAGIC        email,
# MAGIC        gender,
# MAGIC        hiredOn,
# MAGIC        username,
# MAGIC        password
# MAGIC FROM raw_population;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM workflows.`2-silver`.persons
