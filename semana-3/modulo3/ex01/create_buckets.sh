#!/bin/bash
aws s3api create-bucket \
    --bucket 42sp-lkenji-o-bucket-converted \
    --region us-east-1
    
aws s3api create-bucket \
    --bucket 42sp-lkenji-o-bucket \
    --region us-east-1
