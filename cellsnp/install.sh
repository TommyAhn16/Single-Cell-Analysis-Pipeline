#!/bin/bash
source /root/anaconda3/etc/profile.d/conda.sh 
conda init bash
conda create -y --name myenv
conda activate myenv
conda config --add channels bioconda
conda config --add channels conda-forge
conda install -y cellsnp-lite
/home/ec2-user/aws/install
aws configure set aws_access_key_id AKIA5D6X22D42NHKFCDC
aws configure set aws_secret_access_key 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
aws configure set region ap-northeast-2
aws configure set output json
conda install -y -c anaconda boto3