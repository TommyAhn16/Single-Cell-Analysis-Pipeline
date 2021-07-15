FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN chmod +x ./command.sh
RUN yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y python3.7 && \
    pip3 install -r requirements.txt && \
    chmod +x ./command.sh && \
    rm -rf ./Dockerfile