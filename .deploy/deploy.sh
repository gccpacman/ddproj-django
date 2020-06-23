#!/bin/bash

cd "$(dirname "$0")"

echo "1. Copy source code to host:"
scp -r ../* tc1:/root/ddproj-django/

echo "2. Start docker compose:"
ssh tc1 "cd /root/ddproj-django/.deploy/prod; docker-compose up -d"
