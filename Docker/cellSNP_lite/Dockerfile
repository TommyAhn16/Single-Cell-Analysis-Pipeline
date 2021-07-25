FROM amazonlinux:2
WORKDIR /home/ec2-user
COPY . .
RUN chmod +x ./command.sh && \
    # Install packages for Linux os
    yum update -y && \
    yum install -y vim && \
    yum install -y gzip && \
    yum install -y unzip && \
    # Install Anaconda 3 (2021.05)
    curl -O https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh && \
    bash Anaconda3-2021.05-Linux-x86_64.sh -b && \
    # Download AWS CLI 2 (latest version)
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip ./awscliv2.zip && \
    ./aws/install && \
    # Setup Conda environment
    source /root/anaconda3/etc/profile.d/conda.sh && \
    conda init bash && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda create -n CSP cellsnp-lite && \
    conda activate CSP && \
    conda install -y python=3.7 && \
    # Clean up
    rm -rf ./awscliv2.zip && \
    rm -rf ./Anaconda3-2021.05-Linux-x86_64.sh && \
    rm -rf ./Dockerfile

