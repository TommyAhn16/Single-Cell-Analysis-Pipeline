#!/bin/bash
aws configure set aws_access_key_id $AWS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set region $REGION
aws configure set output json
source /root/anaconda3/etc/profile.d/conda.sh
conda init bash
conda activate CSP
python3 cellsnp_lite.py