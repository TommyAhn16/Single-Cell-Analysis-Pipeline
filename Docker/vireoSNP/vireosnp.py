import os
import boto3
import subprocess
from subprocess import CalledProcessError
import sys

# Env variables
sample_id = os.environ['SAMPLE_ID']
download_bucket = os.environ['DOWNLOAD_BUCKET']
upload_bucket = os.environ['UPLOAD_BUCKET']
n_donor = os.environ['N_DONOR']

# Function to run shell commands


def run_command(cmd):
    try:
        subprocess.run(f'echo {cmd}', shell=True)
        subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, check=True)
    except CalledProcessError as e:
        print(f"Stderr: {e.stderr}")
        sys.exit()


# Download files from CellSNP result
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} ./{sample_id}_cellSNP"
subprocess.run("echo '###### Downloading Input Files #######' ", shell=True)
run_command(cmd)


# Run command
cell_snp_path = os.path.join(os.getcwd(), f"{sample_id}_cellSNP")
output_path = os.path.join(os.getcwd(), f"{sample_id}")
cmd = f"vireo -c {cell_snp_path} -N {n_donor} -o {output_path}"
subprocess.run("echo '###### Running Main Command #######' ", shell=True)
run_command(cmd)

# Upload output files
s3_resource = boto3.resource('s3')

# Upload function


def upload_obj(s3_resource, bucket_name, path, key):
    if os.path.isdir(path):
        for file in os.listdir(path):
            upload_obj(s3_resource, bucket_name, os.path.join(
                path, file), os.path.join(key, file))
        return
    obj = s3_resource.Bucket(bucket_name).Object(key)
    with open(path, 'rb') as data:
        obj.upload_fileobj(data)
    print(f"{key} uploaded")
    return


subprocess.run("echo '###### Uploading Result Files #######' ", shell=True)
upload_obj(s3_resource, upload_bucket, output_path, sample_id)

# Clean up
subprocess.run("echo '###### Disk Volume Info #######' ", shell=True)
subprocess.run("df -h", shell=True)
subprocess.run(f"rm -rf {output_path}", shell=True)
subprocess.run(f"rm -rf {cell_snp_path}", shell=True)
