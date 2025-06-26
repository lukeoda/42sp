aws lambda invoke \
    --function-name "packaged_lambda" \
    --invocation-type RequestResponse \
    --payload '{}' \
    --cli-binary-format raw-in-base64-out \
    --endpoint-url http://localhost:4566 \
    "./response.json"
