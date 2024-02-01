# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Handling Parameters/Arguments in and across Notebooks
# MAGIC ### Helpful when
# MAGIC * Doing exploratory analysis
# MAGIC * Reusing code
# MAGIC * Calling notebooks from an API or scheduler
# MAGIC * Executing complex workflows
# MAGIC <br><br>
# MAGIC <img src="https://raw.githubusercontent.com/ebrire/images/main/databricks/tools-icon.png"/>
# MAGIC <br>

# COMMAND ----------

# MAGIC %md
# MAGIC ## There are a few different tools meant to handle arguments
# MAGIC <br>
# MAGIC * `%run`
# MAGIC * `dbutils`<br>
# MAGIC * Jobs API<br>
# MAGIC * Widgets<br>
# MAGIC * `getArgument`<br>
# MAGIC
# MAGIC ## This notebook will show widgets, `%run`, `dbutils` and `getArgument`
# MAGIC <br>

# COMMAND ----------

# MAGIC %md
# MAGIC # Parameters may have an interactive interface (widgets)
# MAGIC <br>
# MAGIC <img src="https://docs.databricks.com/_images/widget-dropdown.png"/>
# MAGIC <br><br>

# COMMAND ----------

# DBTITLE 1,Remove All Widgets
dbutils.widgets.removeAll()

# COMMAND ----------

# DBTITLE 1,Generic Diamonds dataset
diamonds = spark.read.format("csv").option("header", "true").option("inferSchema", "true")
diamonds = diamonds.load("dbfs:/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
diamonds.createOrReplaceTempView("v_diamonds")

# COMMAND ----------

# DBTITLE 1,Let's create a dropdown widget
colors = spark.sql("SELECT DISTINCT color FROM v_diamonds ORDER BY color").rdd.map(lambda row : row[0]).collect()
dbutils.widgets.dropdown("color", colors[0], [str(x) for x in colors], "Select a color" )

# COMMAND ----------

# DBTITLE 1,Let's create a text widget
dbutils.widgets.text(name="clarity", defaultValue="%", label = "Select a clarity level" )

# COMMAND ----------

# DBTITLE 1,Recommended way to use the values from widgets as parameters in a SQL query
# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM v_diamonds
# MAGIC WHERE color     =   getArgument("color")    
# MAGIC AND   clarity LIKE  getArgument("clarity")  

# COMMAND ----------

# DBTITLE 1,Using the widget values the old way
# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM v_diamonds
# MAGIC WHERE color     =   "$color"    
# MAGIC AND   clarity LIKE  "$clarity"  

# COMMAND ----------

# MAGIC %md 
# MAGIC # Passing Arguments BETWEEN Notebooks
# MAGIC <img src="https://github.com/ebrire/images/raw/main/databricks/Notebooks-Parameters.png" width="700"/>
# MAGIC

# COMMAND ----------

# DBTITLE 1,Invoke via %run
# MAGIC %run ./Notebook-Sub-01 $p1="ABC"

# COMMAND ----------

# DBTITLE 1,Invoke via dbutils
result = dbutils.notebook.run( "./Notebook-Sub-02", 60, { "p1" : "123", "p2" : getArgument("color") } )

# COMMAND ----------

# DBTITLE 1,Value returned from the child notebook
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC # For further exploration
# MAGIC <b>Widgets:</b> https://docs.databricks.com/notebooks/widgets.html<br>
# MAGIC <b>Workflows:</b> https://docs.databricks.com/notebooks/notebook-workflows.html<br>
# MAGIC <b>Spark pipelines:</b> https://databricks.com/blog/2016/08/30/notebook-workflows-the-easiest-way-to-implement-apache-spark-pipelines.html<br>
# MAGIC <b>Jobs API:</b> https://docs.databricks.com/dev-tools/api/latest/jobs.html<br>
# MAGIC <br>This notebook: Version 0.1 - 2021-Jan-27 - Eugenio Reis
