#!/bin/bash
/home/ec2-user/aws/install
aws configure set aws_access_key_id $AWS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set region $REGION
aws configure set output json
python3 /home/ec2-user/cellsnp.py
                                  