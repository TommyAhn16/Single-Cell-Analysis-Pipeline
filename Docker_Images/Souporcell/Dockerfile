FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN chmod +x ./command.sh && \
    chmod +x ./setup.sh && \
    # Install Anaconda 3 (2021.05)
    curl -O https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh && \
    bash Anaconda3-2021.05-Linux-x86_64.sh -b && \
    # Install packages for linux os
    yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y gcc && \
    yum install -y tar && \
    # Download referance fasta file
    curl -O https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz && \
    tar -xzvf refdata-gex-GRCh38-2020-A.tar.gz && \
    mv ./refdata-gex-GRCh38-2020-A/fasta ./ && \
    # Run setup commands
    ./setup.sh && \
    # Clean up
    rm -rf ./setup.sh && \
    rm -rf ./Anaconda3-2021.05-Linux-x86_64.sh && \
    rm -rf ./Dockerfile && \
    rm -rf ./refdata-gex-GRCh38-2020-A.tar.gz && \
    rm -rf ./refdata-gex-GRCh38-2020-A