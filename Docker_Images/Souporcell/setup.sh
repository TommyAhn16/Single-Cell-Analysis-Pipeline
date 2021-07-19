#!/bin/bash
# Install Souporcell repo
git clone https://github.com/wheaton5/souporcell.git
# Install Anaconda and packages
source /root/anaconda3/etc/profile.d/conda.sh
conda init bash
conda env create -f /home/ec2-user/souporcell/souporcell_env.yaml
conda activate souporcell
conda install -y -c conda-forge awscli
# Install Rust and compile
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env
cd /home/ec2-user/souporcell/souporcell && cargo build --release
cd /home/ec2-user/souporcell/troublet && cargo build --release
# Install additional tools
cd /home/ec2-user
mkdir tools
# Minimap2 installation
yum install -y zlib-devel
wget https://github.com/lh3/minimap2/archive/v2.7.tar.gz
tar -xzvf v2.7.tar.gz
cd minimap2-2.7
make
cd ..
mv ./minimap2-2.7/minimap2 ./tools/.
rm -rf v2.7.tar.gz
rm -rf minimap2-2.7
# bedtools2 installation
wget https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools.static.binary
mv bedtools.static.binary tools/bedtools
chmod 777 tools/bedtools
# Freebayes installation
wget https://github.com/ekg/freebayes/releases/download/v1.3.1/freebayes-v1.3.1
mv freebayes-v1.3.1 ./tools/freebayes
chmod 777 ./tools/freebayes
# Vartrix installation
wget https://github.com/10XGenomics/vartrix/releases/download/v1.1.22/vartrix_linux
mv vartrix_linux ./tools/vartrix
chmod 777 ./tools/vartrix