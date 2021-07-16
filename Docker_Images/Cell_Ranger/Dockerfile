FROM amazonlinux:2
WORKDIR /home/ec2-user
ADD cellranger-5.0.1.tar.gz /opt/
ADD refdata-gex-GRCh38-2020-A.tar.gz /home/ec2-user/
COPY requirements.txt /home/ec2-user/requirements.txt
COPY aws /home/ec2-user/aws
COPY cellranger.py /home/ec2-user/cellranger.py
COPY command.sh /home/ec2-user/command.sh
RUN yum update -y && \
    yum install -y vim && \
    yum install -y tar && \
    yum install -y gzip && \
    yum install -y python3.7 && \
    pip3 install -r /home/ec2-user/requirements.txt && \
    chmod +x /home/ec2-user/command.sh