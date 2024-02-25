from flask import Flask
from seleniumwire import webdriver
import json
import logging
import mysql.connector
from mysql.connector import Error
import pandas as pd
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/network_info")
def network():
  options = {
    'enable_har': True  # Capture HAR data, retrieve with driver.har
  }
  driver = webdriver.Chrome(seleniumwire_options=options)
  values = json.loads(driver.har)
  return (values["log"]["entries"][1]["request"]["method"], values["log"]["entries"][1]["response"]['content']['text'], values["log"]["entries"][1]["request"]["url"])

@app.route("/after_request_logging")
def after_request_logging():
  options = {
    'enable_har': True  # Capture HAR data, retrieve with driver.har
  }
  driver = webdriver.Chrome(seleniumwire_options=options)
  response = json.loads(driver.har)
  return response

@app.route("/test_with_pyshark")
def test_with_pyshark():
  import pyshark 
  capture = pyshark.LiveCapture(interface='en0', bpf_filter='http')
  capture.sniff(timeout=5)
  print(capture)
  print(len(capture))
  print(capture[len(capture)-1])
  for packet in capture.sniff_continuously(packet_count=len(capture)):
      print('Just arrived:', packet.ip.field_names)
      print('Packet length:', packet.length)
  return capture

def create_db_connection(host_name, user_name, user_password, db_name):
  connection = None
  try:
      connection = mysql.connector.connect(
          host=host_name,
          user=user_name,
          passwd=user_password,
          database=db_name
      )
      print("MySQL Database connection successful")
  except Error as err:
      print(f"Error: '{err}'")

  return connection

def execute_query(connection, query):
  cursor = connection.cursor()
  try:
      cursor.execute(query)
      connection.commit()
      print("Query successful")
  except Error as err:
      print(f"Error: '{err}'")

def read_query(connection, query):
  cursor = connection.cursor()
  result = None
  try:
      cursor.execute(query)
      result = cursor.fetchall()
      return result
  except Error as err:
      print(f"Error: '{err}'") 


@app.route("/incrementPricing") 
def incrementPricing():
  connection = create_db_connection('localhost', 'root', 'Pik@chu1423', 'chatgdp')
  check_model_name = "gpt-4-0125-preview"
  if check_model_name == "gpt-4-0125-preview":
    increment = 'UPDATE model_values SET price = price + 21*0.04 WHERE model_name = "gpt-4-0125-preview"'
    execute_query(connection, increment)
  elif check_model_name == "gpt-3.5-turbo-0125":
    increment = 'UPDATE model_values SET price = price + 24*0.09 WHERE model_name = "gpt-3.5-turbo-0125"'
    execute_query(connection, increment)
  elif check_model_name == "gpt-4-32k":
    increment = 'UPDATE model_values SET price = price + 23*0.18 WHERE model_name = "gpt-4-32k"'
    execute_query(connection, increment)
  elif check_model_name == "davinci-002":
    increment = 'UPDATE model_values SET price = price + 22*0.024 WHERE model_name = "davinci-002"'
    execute_query(connection, increment)
  else:
    increment = 'UPDATE model_values SET price = price + 21*0.04 WHERE model_name = "gpt-4-0125-preview"'
    execute_query(connection, increment)
    increment = 'UPDATE model_values SET price = price + 24*0.09 WHERE model_name = "gpt-3.5-turbo-0125"'
    execute_query(connection, increment)
    increment = 'UPDATE model_values SET price = price + 23*0.18 WHERE model_name = "gpt-4-32k"'
    execute_query(connection, increment)
    increment = 'UPDATE model_values SET price = price + 22*0.024 WHERE model_name = "davinci-002"'
    execute_query(connection, increment)
  select_query = "SELECT * from model_values"
  result = read_query(connection, select_query)
  results = []
  for row in result:
    results.append(row)
  print(results)
  return results


if __name__ == "__main__":
  app.debug = True
  app.run()
