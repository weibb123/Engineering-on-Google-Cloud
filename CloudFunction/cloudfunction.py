import functions_framework
from google.cloud import pubsub_v1, storage
import json

@functions_framework.http
def request_http(request):
    # banned countries..
    banned_countries = ["North Korea", "Iran", "Cuba", "Myanmar", "Iraq", "Libya", "Sudan", "Zimbabwe", "Syria"]

    # Initialize pub/sub publisher
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("true-source-329719", 'homework3')

    # only request GET
    file_name = request.path.lstrip("/")
    if request.method != 'GET':
        print("only GET method implemented")
        return ("501-Method Not Implemented", 501)
    
    # Initialize the GCS client / Bucket Info
    client = storage.Client()
    bucket_name = "weimaihomework2"
    bucket = client.bucket(bucket_name)
    request_blob = 'homework2/dir/' + file_name

    if not file_name:
        print("404-File not specified")
        return '404, no file'
    
    # check illegal country information
    country = request.headers.get('X-country')

    dict = {
        "country": country
    }
    data = json.dumps(dict).encode('utf-8')
    
    # check if country is in the list of banned countries
    if country in banned_countries:
        # publish a message to the pub/sub topic
        ip = publisher.publish(topic_path, data=data)
        print(ip)

        # logging
        print("Permission denied, 400")

        # return 400 permission error
        return ("Permission denied", 400)
    
    try:
        blob = bucket.get_blob(request_blob)
        return blob.download_as_string(), 200
    except:
        print("File Not Found 404")
        return ("404-File Not Found, 404")


   
    
   





    