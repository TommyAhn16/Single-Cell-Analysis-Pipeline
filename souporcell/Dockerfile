FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN bash Anaconda3-2021.05-Linux-x86_64.sh -b && \
    yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y gcc && \
    yum install -y tar && \
    chmod +x ./command.sh && \
    chmod +x ./setup.sh && \
    ./setup.sh && \
    rm -rf ./setup.sh && \
    rm -rf ./Anaconda3-2021.05-Linux-x86_64.sh && \
    rm -rf ./Dockerfile