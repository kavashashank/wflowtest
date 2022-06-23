# Databricks notebook source
# this notebook is part of the ClickIngest Workflow
#


# COMMAND ----------

# imports  
#
#

from random import randint
from time import sleep
import os


# COMMAND ----------

# connect to external API 
# retrieve data for last 12 months
# 
#

def ingest_all_orders():

  
  
  if randint(1,100) > 95:
    raise ConnectionError("connection refused / external API")
    

# COMMAND ----------

sleep(randint(5,25))
ingest_all_orders()

# COMMAND ----------


