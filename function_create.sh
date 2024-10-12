#!/bin/bash

if [ -z "$AWS_ROLE_ARN" ]; then
    echo "AWS_ROLE_ARN is not set"
    exit 1
fi
if [ -f "archive.zip" ]; then
    rm -rf archive.zip
fi
find . -name "__pycache__" -exec rm -rf {} +
find . -name ".DS_Store" -exec rm -rf {} +
zip -r archive.zip . -x "*.git*" -x ".env.example" -x "*.sh"
aws lambda create-function --function-name CrawlProducts \
    --runtime python3.12 \
    --role $AWS_ROLE_ARN \
    --handler crawl.crawl_products_handler \
    --zip-file fileb://archive.zip