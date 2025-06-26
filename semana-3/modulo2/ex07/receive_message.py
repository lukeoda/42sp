import boto3
import sys


url_queue = sys.argv[1]	  

def receive_messages(queue, max_number, wait_time):
    print('Aguardando mensagens....')
    for message in queue.receive_messages(
            MessageAttributeNames=["All"],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
            QueueUrl=url_queue,
        ):
       
        print(f"Mensagem recebida: 'message': '{message.body}'")
        message.delete()


def main():  
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='42sp-lkenji-o-queue')
    # sqs = boto3.client("sqs", endpoint_url=url_queue, region_name="us-east-1")
    #queue = sqs.get_queue_by_name(QueueName='42sp-lkenji-o-queue')
    while(True):
        receive_messages(queue, 100, 600)
        
if __name__ == "__main__":
    main()
