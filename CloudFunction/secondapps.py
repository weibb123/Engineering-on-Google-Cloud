from google.cloud import pubsub_v1

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path("true-source-329719", "homework3-sub")


def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received: {message}")
    message.ack()

with subscriber:

    sub = subscriber.subscribe(subscription_path, callback=callback)
    print(f"listening messages {subscription_path}..\n")

    try:
        sub.result()
    
    except Exception as e:
        print(f"exception {e} occurred")
        sub.cancel()