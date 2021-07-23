FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN \
    # Install packages for linux os
    yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y unzip && \
    # Download Python and dependencies
    yum install -y python3.7 && \
    pip3 install --no-cache-dir -r requirements.txt && \
    # Make script executable
    chmod +x ./command.sh && \
    # Download AWS CLI 2 (latest version)
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    # Clean up
    rm -rf ./awscliv2.zip && \
    rm -rf ./Dockerfile