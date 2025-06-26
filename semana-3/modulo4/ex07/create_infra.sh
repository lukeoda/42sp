#!/bin/bash
aws s3api create-bucket \
    --bucket 42sp-lkenji-o-bucket-converted \
    --region us-east-1
    
aws s3api wait bucket-exists \
    --bucket 42sp-lkenji-o-bucket-converted

aws s3api create-bucket \
    --bucket 42sp-lkenji-o-bucket \
    --region us-east-1

aws s3api wait bucket-exists \
    --bucket 42sp-lkenji-o-bucket

mkdir package

docker run --rm -v "$PWD":/var/task \
    --entrypoint /bin/sh \
    public.ecr.aws/lambda/python:3.13 \
    -c "pip install pillow -t package/"

cp lambda_convert.py package/
(cd package && zip -r ../package.zip .)
 
ARN_LAMBDA=$(aws lambda create-function \
    --function-name lambda_convert \
    --runtime python3.13 \
    --handler 'lambda_convert.lambda_handler' \
    --zip-file fileb://package.zip \
    --role arn:aws:iam::992846590112:role/D04-LambdaS3AccessRole \
    --no-cli-pager \
    --query 'FunctionArn' --output text)

rm -rf "./package"
rm -rf "./package.zip"

aws lambda wait function-active-v2 --function-name lambda_convert

BUCKET_NAME="42sp-lkenji-o-bucket"

aws lambda add-permission \
    --function-name "$ARN_LAMBDA" \
    --statement-id "S3InvokeLambda_$(date +%s)" \
    --action "lambda:InvokeFunction" \
    --principal "s3.amazonaws.com" \
    --source-arn "arn:aws:s3:::$BUCKET_NAME" \
    --source-account "$(aws sts get-caller-identity --query Account --output text)" \
    --output text



NOTIFICATION_CONFIGURATION=$(cat <<EOF
{
  "LambdaFunctionConfigurations": [
    {
      "LambdaFunctionArn": "$ARN_LAMBDA",
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
}
EOF
)

aws s3api put-bucket-notification-configuration \
  --bucket "$BUCKET_NAME" \
  --notification-configuration "$NOTIFICATION_CONFIGURATION"