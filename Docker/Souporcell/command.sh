#!/bin/bash
echo export PATH='"/home/ec2-user/souporcell:$PATH"' >> ~/.bashrc
echo export PATH='"/home/ec2-user/tools:$PATH"' >> ~/.bashrc
echo export PATH='"/home/ec2-user/souporcell/troublet/target/release:$PATH"' >> ~/.bashrc
echo export PATH='"/home/ec2-user/souporcell/souporcell/target/release:$PATH"' >> ~/.bashrc
source ~/.bashrc
source /root/anaconda3/etc/profile.d/conda.sh
conda init bash
conda activate souporcell
aws configure set aws_access_key_id $AWS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws configure set region $REGION
aws configure set output json
python3 ./SPC.py