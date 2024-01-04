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

