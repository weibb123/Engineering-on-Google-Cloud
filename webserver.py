from flask import Flask, request
from google.cloud import storage, pubsub_v1
import google.cloud.logging 
import logging # google cloud logging
import json
from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import text

project_id = <your_project_id>
region = <your_region>
instance_name = <your_db_name>
pw = <your_pw>
banned_countries = ["North Korea", "Iran", "Cuba", "Myanmar", "Iraq", "Libya", "Sudan", "Zimbabwe", "Syria"]

instance_connection_name = f"{project_id}:{region}:{instance_name}"
print(f"Your instance connection name is: {instance_connection_name}")
DB_USER = <your_db_user>
DB_PASS = <your_db_user_password>
DB_NAME = <your_db_name>

## SQL STUFF ##
# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        instance_connection_name,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

## SQL STUFF ##

app = Flask(__name__)

# Initialize google cloud loggin client
logging_client = google.cloud.logging.Client()

# config log handler
log_name = 'hw4-log'
logger = logging_client.logger(log_name)


@app.route('/<path:filename>', methods=['GET'])
def get_file(filename):
    db_conn = pool.connect()
    insert_user = text(
        "INSERT INTO IP_TABLE (country, gender, age, income, client_ip, time_of, requested_file) VALUES (:country, :gender, :age, :income, :client_ip, :time_of, :file)",
        )
    insert_error = text(
        "INSERT INTO ERROR_TABLE (time_of, requested_file, error_code) VALUES (:time, :file, :code)"
        )
    insert_ban = text(
        "INSERT INTO BAN_TABLE (is_banned, country) VALUES (:ban, :country)"
    )

    # Initialize google cloud storage client
    storage_client = storage.Client()

    bucket_name = "weimaihomework2"
    bucket = storage_client.bucket(bucket_name)
    request_blob = 'homework2/dir/' + filename

    blob = bucket.blob(request_blob)

    country = request.headers.get("X-country")
    want_ip = request.headers.get("X-client-IP")
    gender = request.headers.get("X-gender")
    age = request.headers.get("X-age")
    income = request.headers.get("X-income")
    time = request.headers.get("X-time")

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('true-source-329719', 'homework3')
      
    if not filename:
        logger.log_text("File not specified")
        return '404, no file'
    
    dict = {
        "country": country
    }
    data = json.dumps(dict).encode('utf-8')

    if country in banned_countries:
        # publish message to pubsub
        ip = publisher.publish(topic_path, data=data)
        logger.log_text("Permission denied illegal country, 400")
        # insert entries into table
        db_conn.execute(insert_error, parameters={"time": time, "file":filename, "code": 400})
        db_conn.execute(insert_ban, parameters={"ban": 'TRUE', "country":country})
        db_conn.commit()
        return ("Permission denied, 400")
    
    elif blob.exists():
        print("file found")
        logger.log_text("file found, 200")
        db_conn.execute(insert_user, parameters={"country": country, "gender": gender, "age": age, "income": income, "client_ip": want_ip, "time_of":time, "file": filename})
        db_conn.execute(insert_ban, parameters={"ban": 'FALSE', "country":country})
        db_conn.commit()
        return blob.download_as_text(), 200
        
    else:
        logger.log_text("file not found")
        db_conn.execute(insert_error, parameters={"time": time, "file":filename, "code": 404})
        db_conn.commit()
        return "File not found, 404"
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
