import boto3
import sys

url_queue = sys.argv[1]	

def send_message(queue, message_body, message_attributes=None):
    if not message_attributes:
        message_attributes = {}
        
    response = queue.send_message(
        MessageBody=message_body, MessageAttributes=message_attributes, QueueUrl=url_queue
    )
    print(response)
    return response


def main():

    msg_body = sys.argv[2]	    
    
    sqs = boto3.client("sqs", endpoint_url=url_queue, region_name="us-east-1")
    
    send_message(sqs, msg_body)
    

if __name__ == "__main__":
    main()

