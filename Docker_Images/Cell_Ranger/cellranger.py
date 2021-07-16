import os
import boto3
import subprocess
import sys

# Env variables
download_bucket = os.environ['download_bucket']
upload_bucket = os.environ['upload_bucket']
sample_id = os.environ['sample_id']
core = os.environ['core']
memory = os.environ['memory']
expect_cells = os.environ['expect_cells']

# Variables
sample_file_path = os.path.join(os.getcwd(), f"{sample_id}_samples")
cellranger = "/opt/cellranger-5.0.1/cellranger"
ref_file = "/home/ec2-user/refdata-gex-GRCh38-2020-A"

# Function to run shell commands


def run_command(cmd):
    try:
        subprocess.run(f'echo {cmd}', shell=True)
        subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Stderr: {e.stderr}")
        sys.exit()


# S3 client, resource
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# Download samples: AWS CLI
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} {sample_file_path}"
run_command(cmd)

# chek if files are downloaded
subprocess.run(f"ls -lh {sample_file_path}")
subprocess.run("df -h")

# Run command
cmd = f"{cellranger} count --id={sample_id} --fastqs={sample_file_path} --transcriptome={ref_file} --localcores={core} --localmem={memory} --expect-cells={expect_cells}"
run_command(cmd)

# Upload output files
output_folder_path = os.path.join(os.getcwd(), sample_id)
files = os.listdir(output_folder_path)

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
    return


# Upload log
if "_log" in files:
    obj_key = os.path.join(sample_id, "_log")
    obj_path = os.path.join(os.path.join(os.getcwd(), sample_id), "_log")
    upload_obj(s3_resource, upload_bucket, obj_path, obj_key)

# Upload outs
if "outs" in files:
    outs_path = os.path.join(output_folder_path, "outs")
    outs_files = os.listdir(outs_path)
    outs_key = os.path.join(sample_id, "outs")
    for file in outs_files:
        if file != "analysis":
            file_path = os.path.join(outs_path, file)
            file_key = os.path.join(outs_key, file)
            upload_obj(s3_resource, upload_bucket, file_path, file_key)

# Upload metrics_summary_json
json_file = "metrics_summary_json.json"
counter_path = os.path.join(output_folder_path, "SC_RNA_COUNTER_CS")
for dirpath, dirnames, filenames in os.walk(counter_path):
    for file in filenames:
        if file == json_file:
            json_path = os.path.join(os.path.join(
                output_folder_path, os.path.join(dirpath)), file)
            json_key = os.path.join(sample_id, json_file)
            upload_obj(s3_resource, upload_bucket, json_path, json_key)

# Clean up
subprocess.run("df -h", shell=True)
subprocess.run(f"rm -rf {os.path.join(os.getcwd(),sample_id)}", shell=True)
subprocess.run(f"rm -rf {sample_file_path}", shell=True)
subprocess.run("df -h", shell=True)
