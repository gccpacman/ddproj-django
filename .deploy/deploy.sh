#!/bin/bash

cd "$(dirname "$0")"

echo "1. Copy source code to host:"
# rsync -avz --progress --exclude '.deploy' --exclude '.git' --exclude 'data' --exclude '*.pyc' --exclude '**/__pycache__/' ../* tc6:/home/ubuntu/ddproj-django/
rsync -avz --progress --exclude '.deploy' --exclude '.git' --exclude 'data' --exclude '*.pyc' --exclude '**/__pycache__/' ../* tc1:/root/ddproj-django/

echo "2. docker build"
ssh tc1 "cd /root/ddproj-django/.deploy/prod; docker-compose build"

echo "3. restart app"
ssh tc1 "cd /root/ddproj-django/.deploy/prod; docker-compose up -d"

