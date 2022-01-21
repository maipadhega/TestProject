from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os
import uuid
# Retrieve the connection string from an environment
# variable named AZURE_STORAGE_CONNECTION_STRING
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
connect_str = "DefaultEndpointsProtocol=https;AccountName=firststoragebyvivek;AccountKey=JFJ+CHFS/n8z0l+qZos18frwFbm2k2rdRtFuSJ3fF03TTdX3yriEHotDpdyrR+fSRBjO5MzNzzlK5ig6BeWatQ=="
# Create a unique name for the queue
q_name = "queue-" + str(uuid.uuid4())

# Instantiate a QueueClient object which will
# be used to create and manipulate the queue
print("Creating queue: " + q_name)
queue_client = QueueClient.from_connection_string(connect_str, q_name)

# Create the queue
queue_client.create_queue()

# Setup Base64 encoding and decoding functions
base64_queue_client = QueueClient.from_connection_string(
                            conn_str=connect_str, queue_name=q_name,
                            message_encode_policy=BinaryBase64EncodePolicy(),
                            message_decode_policy=BinaryBase64DecodePolicy()
                        )
message = u"Hello World"
print("Adding message: " + message)
queue_client.send_message(message)
