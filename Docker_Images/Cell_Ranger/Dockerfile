FROM amazonlinux:2
ADD cellranger-5.0.1.tar.gz /opt/
WORKDIR /home/ec2-user
COPY requirements.txt /home/ec2-user/requirements.txt
COPY cellranger.py /home/ec2-user/cellranger.py
COPY command.sh /home/ec2-user/command.sh
RUN chmod +x /home/ec2-user/command.sh && \
    # Install packages for Linux os
    yum update -y && \
    yum install -y vim && \
    yum install -y tar && \
    yum install -y gzip && \
    yum install -y unzip && \
    # Download AWS CLI 2 (latest version)
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip ./awscliv2.zip && \
    ./aws/install && \
    # Download referance file
    curl -O https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz && \
    tar -xzvf refdata-gex-GRCh38-2020-A.tar.gz && \
    # Download Python and required packages
    yum install -y python3.7 && \
    pip3 install -r /home/ec2-user/requirements.txt && \
    # Clean up
    rm -rf ./refdata-gex-GRCh38-2020-A.tar.gz && \
    rm -rf ./awscliv2.zip