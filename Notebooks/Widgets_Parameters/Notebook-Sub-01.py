# Databricks notebook source
displayHTML( """
  <p style="font-size:22px">
  A notebook invoked with '%run' uses the same session as the master notebook<br>
  The execution is immediate, since there's no need to instantiate a new session<br>
  The child notebook has direct access to all variables and widgets created in the master<br><br>
  Regardless, arguments can be passed and they are a safe practice ✅👍🏼<br></p>
  <p style="font-size:22px; font-family: Courier New">
  📝 <b>NOTE: getArgument and dbutils.widgets.get are synonyms</b>
  </p>
"""  )

# COMMAND ----------

print("The value of 'color' was NOT passed, it's part of the master session  ===> " + getArgument("color"))
print("Retrieving the value of 'color' via dbutils.widgets.get()             ===> " + dbutils.widgets.get("color"))
print()
print("The parameter p1 was passed, it did NOT come as part of the session   ===> " + getArgument("p1"))
print("The parameter p1 can also be read using dbutils.widgets.get()         ===> " + dbutils.widgets.get("p1"))
print()

