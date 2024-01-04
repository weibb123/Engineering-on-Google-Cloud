Cloud function

Cloud functions respond to http requests, pubsub event, cloud storage events

```
import functions_framework
from google.cloud import pubsub_v1, storage
import json

@functions_framework.http
def request_http(request):
   return ...
```

When it comes to logging messages. Cloud functions have built-in print statement.
By printing the message, it logs the message onto google cloud function logging.


#### Deployment method

```
gcloud functions deploy hw3cloudfunction --runtime=python311 --region=us-east1 --source=. --entry-point=request_http --trigger-http --allow-unauthenticated
```

#### Including Pub/sub
To integrate pub/sub into our application. We need to build a second app that will be the subscriber.

Pub/sub comes in handy since they can communicate between different cloud functions or different part of software system.

Pros: falut tolerance, real-time processing(subscribers react to live messages as they arrive)

1. Create pub/sub topic on google cloud
2. App(publisher) for publishing message and second app(subscriber) for receiving message

```
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_id)
```

second app

```
subscriber = pubsub_v1.SubscriberClient()
sub_path = Subscriber.subscription_path(project_name, topic_id)
```



