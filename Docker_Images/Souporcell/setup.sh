#!/bin/bash
source /root/anaconda3/etc/profile.d/conda.sh
conda init bash
conda env create -f /home/ec2-user/souporcell/souporcell_env.yaml
conda activate souporcell
conda install -y -c conda-forge awscli
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env
cd /home/ec2-user/souporcell/souporcell && cargo build --release
cd /home/ec2-user/souporcell/troublet && cargo build --release
echo export PATH='"/home/ec2-user/souporcell:$PATH"' >> ~/.bashrc
echo export PATH='"/home/ec2-user/tools:$PATH"' >> ~/.bashrc
echo export PATH='"/home/ec2-user/souporcell/troublet/target/release:$PATH"' >> ~/.bashrc
echo export PATH='"/home/ec2-user/souporcell/souporcell/target/release:$PATH"' >> ~/.bashrc
source ~/.bashrc