import json

def lambda_handler(event, context):
    '''
    aws lambda create-function \
    --function-name first_lambda \
    --runtime python3.13 \
    --handler 'first_lambda.lambda_handler' \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --endpoint-url http://localhost:4566    
    '''
    return json.dumps({'message': 'Hello from lambda!'})