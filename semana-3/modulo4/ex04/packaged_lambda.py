import json
import PIL

def lambda_handler(event, context):
    '''
    aws lambda create-function \
    --function-name first_lambda \
    --runtime python3.13 \
    --handler 'first_lambda.lambda_handler' \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --endpoint-url http://localhost:4566    
    
    aws lambda delete-function \
    --function-name packaged_lambda
    
    
    aws lambda add-permission \
    --function-name packaged_lambda \
    --statement-id s3-invocation-permission \
    --action "lambda:InvokeFunction" \
    --principal s3.amazonaws.com \
    --source-arn "arn:aws:s3:::42sp-lkenji-o-bucket" \
    --endpoint-url=http://localhost:4566
    '''
    print("Lambda invocada com sucesso!")
    return json.dumps({'message': PIL.__version__})