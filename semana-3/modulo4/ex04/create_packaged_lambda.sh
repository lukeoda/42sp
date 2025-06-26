
aws lambda create-function \
    --function-name packaged_lambda \
    --runtime python3.13 \
    --handler 'packaged_lambda.lambda_handler' \
    --zip-file fileb://package.zip \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --endpoint-url http://localhost:4566 \
    --no-cli-pager   

rm -rf "./package"
rm -rf "./package.zip"