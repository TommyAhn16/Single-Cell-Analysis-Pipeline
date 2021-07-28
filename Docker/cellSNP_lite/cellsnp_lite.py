import os
import subprocess
import sys

# Env variables
sample_id = os.environ['SAMPLE_ID']
download_bucket = os.environ['DOWNLOAD_BUCKET']
upload_bucket = os.environ['UPLOAD_BUCKET']
threads = os.environ['THREADS']  # 22
min_MAF = os.environ['MIN_MAF']  # 0.1
min_count = os.environ['MIN_COUNT']  # 100

# Variables
home_dir = "/home/ec2-user"
mnt_dir = "/home/ec2-user/vol_mnt"

# Function to run shell commands


def run_command(cmd):
    try:
        subprocess.run(f'echo {cmd}', shell=True)
        subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Stderr: {e.stderr}")
        sys.exit()


# File directory
download_path = os.path.join(mnt_dir, sample_id)
output_dir = os.path.join(mnt_dir, f"{sample_id}_cellSNP")

# Download files
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} {download_path}"
subprocess.run("echo '###### Downloading Input Files #######' ", shell=True)
run_command(cmd)
subprocess.run("echo '###### Checking Free Disk Volume #######' ", shell=True)
subprocess.run("df -h", shell=True)

# Bam, barcode path
bamfile_path = ""
barcode_path = ""
for dirpath, dirnames, filenames in os.walk(download_path):
    for file in filenames:
        if file == "possorted_genome_bam.bam":
            bamfile_path = os.path.join(dirpath, file)
        elif file == "barcodes.tsv.gz":
            cmd = f"gunzip {os.path.join(dirpath,file)}"
            run_command(cmd)
            barcode_path = os.path.join(dirpath, "barcodes.tsv")
        elif file == "barcodes.tsv":
            barcode_path = os.path.join(dirpath, file)

# Run command
cmd = f"cellsnp-lite -s {bamfile_path} -b {barcode_path} -O {output_dir} -p {threads} --minMAF {min_MAF} --minCOUNT {min_count} --gzip"
subprocess.run("echo '###### Running Main Command #######' ", shell=True)
run_command(cmd)

# Upload output files
cmd = f"aws s3 sync {output_dir} s3://{upload_bucket}/{sample_id}"
subprocess.run("echo '###### Uploading Result Files #######' ", shell=True)
run_command(cmd)

# Clean up
subprocess.run("echo '###### Checking Free Disk Volume #######' ", shell=True)
subprocess.run("df -h", shell=True)
subprocess.run(f"rm -rf {download_path}", shell=True)
subprocess.run(f"rm -rf {output_dir}", shell=True)
