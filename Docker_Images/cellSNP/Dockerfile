FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y tar && \
    yum install -y python3.7 && \
    pip3 install cellSNP==0.3.2 &&\
    chmod +x ./command.sh && \
    rm -rf ./Dockerfile