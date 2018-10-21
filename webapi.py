#!/usr/bin/python


import mysql.connector as mariadb
from mysql.connector import Error
from flask import Flask, jsonify
#import json

app = Flask(__name__)

mariadb_connection = mariadb.connect(host='terraform-20181012185152609300000001.cyys4rqwgvrk.eu-west-3.rds.amazonaws.com', port='3306',  user='xxxxx', password='xxxxxx', database='employees') 

Name = "Bezalel"

@app.route('/hello')
def index():
   cursor = mariadb_connection.cursor()
   cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=%s", (Name,))
   #row_headers=[x[0] for x in cursor.description]
  # rows = cursor.fetchall()
   #json_data=[]
   #for result in rv:
   #     json_data.appn(dict(zip(row_headers,result)))
   #return json.dumps(json_data)
   r = [dict((cursor.description[i][0], value)
             for i, value in enumerate(row)) for row in cursor.fetchall()]
   return jsonify({'myQuery' : r})
   obj = json.loads(myQuery)
  

if __name__== '__main__':
   app.run()
