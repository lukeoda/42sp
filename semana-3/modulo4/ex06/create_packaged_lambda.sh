mkdir package

docker run --rm -v "$PWD":/var/task \
    --entrypoint /bin/sh \
    public.ecr.aws/lambda/python:3.13 \
    -c "pip install pillow -t package/"

cp process.py package/
(cd package && zip -r ../package.zip .)
 
aws lambda create-function \
    --function-name process \
    --runtime python3.13 \
    --handler 'process.lambda_handler' \
    --zip-file fileb://package.zip \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --endpoint-url http://localhost:4566 \
    --no-cli-pager   

rm -rf "./package"
rm -rf "./package.zip"

aws lambda wait function-active-v2 --function-name process

BUCKET_NAME="42sp-lkenji-o-bucket"
NOTIFICATION_CONFIGURATION='{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:lambda_convert",
      "Events": [
        "s3:ObjectCreated:*"
      ],
      "Filter": {
        "Key": {
          "FilterRules": [
            {
              "Name": "suffix",
              "Value": ".jpg"
            }
          ]
        }
      }
    }
  ]
}'

aws s3api put-bucket-notification-configuration \
  --bucket "$BUCKET_NAME" \
  --notification-configuration "$NOTIFICATION_CONFIGURATION"