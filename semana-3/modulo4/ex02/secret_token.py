import json

def lambda_handler(event, context):
    '''
    aws lambda create-function \
    --function-name secret_token \
    --runtime python3.9 \
    --zip-file fileb://secret_token.zip \
    --handler secret_token.lambda_handler \
    --role arn:aws:iam::000000000000:role/irrelevant_role \
    --endpoint-url http://localhost:4566    
    '''
    return json.dumps({'flag': 'YOU FOUND THE SECRET'}) 