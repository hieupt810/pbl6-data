#!/bin/bash

if [ -f "archive.zip" ]; then
    rm -rf archive.zip
fi
find . -name "__pycache__" -exec rm -rf {} +
find . -name ".DS_Store" -exec rm -rf {} +
zip -r archive.zip . -x "*.git*" -x ".env.example" -x "*.sh"
aws lambda update-function-code --function-name CrawlProducts \
    --zip-file fileb://archive.zip