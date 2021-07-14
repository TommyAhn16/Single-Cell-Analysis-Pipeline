#!/bin/bash
cd /home/ec2-user
mv /home/ec2-user/cellranger.py /home/ec2-user/vol_mnt/cellranger.py
/home/ec2-user/aws/install
aws configure set aws_access_key_id AKIA5D6X22D42NHKFCDC
aws configure set aws_secret_access_key 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
aws configure set region ap-northeast-2
aws configure set output json
cd /home/ec2-user/vol_mnt
python3 /home/ec2-user/vol_mnt/cellranger.py