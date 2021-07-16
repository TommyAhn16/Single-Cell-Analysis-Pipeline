#!/bin/bash
cd /home/ec2-user
mv /home/ec2-user/cellranger.py /home/ec2-user/vol_mnt/cellranger.py
/home/ec2-user/aws/install
aws configure set aws_access_key_id $AWS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set region $REGION
aws configure set output json
cd /home/ec2-user/vol_mnt
python3 /home/ec2-user/vol_mnt/cellranger.py