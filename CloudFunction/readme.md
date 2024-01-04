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



