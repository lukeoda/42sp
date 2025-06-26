#!/bin/bash
BUCKET_NAME="42sp-lkenji-o-bucket"
NOTIFICATION_CONFIGURATION='{
	"LambdaFunctionConfigurations": [
	  {
		"LambdaFunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:packaged_lambda",
		"Events": [
		  "s3:ObjectCreated:*"
		]
	  }
	]
}'

aws s3api put-bucket-notification-configuration \
  --bucket "$BUCKET_NAME" \
  --notification-configuration "$NOTIFICATION_CONFIGURATION"

if [ $? -eq 0 ]; then
  echo "Gatilho de evento de Lambda adicionado com sucesso ao bucket '$BUCKET_NAME'."
else
  echo "Erro ao adicionar o gatilho de evento de Lambda ao bucket '$BUCKET_NAME'."
fi