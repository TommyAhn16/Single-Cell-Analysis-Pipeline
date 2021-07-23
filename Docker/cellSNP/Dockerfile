FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN chmod +x ./command.sh && \
    # Install packages for Linux os
    yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y tar && \
    yum install -y unzip && \
    # Download Python and required packages
    yum install -y python3.7 && \
    pip3 install cellSNP==0.3.2 &&\
    # Download AWS CLI 2 (latest version)
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip ./awscliv2.zip && \
    ./aws/install && \
    # Clean up
    rm -rf ./Dockerfile && \
    rm -rf ./awscliv2.zip