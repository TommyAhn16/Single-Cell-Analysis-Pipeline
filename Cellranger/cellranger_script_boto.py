import os
import boto3
import re
# Env variables
download_bucket = os.environ['download_bucket']
upload_bucket = os.environ['upload_bucket']
sample_id = os.environ['sample_id']
sample_folder = os.environ['sample_folder']
core = os.environ['core']
memory = os.environ['memory']
expect_cells = os.environ['expect_cells']

# Variables
sample_file_path = os.path.join(os.getcwd(),sample_folder)
cellranger = "/opt/cellranger-5.0.1/cellranger"
ref_file = "/home/ec2-user/refdata-gex-GRCh38-2020-A"

# S3 client, resource
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# Download samples
try:
    os.mkdir(sample_file_path)
except:
    pass
d_bucket = s3_resource.Bucket(download_bucket)
download_files = [obj.key for obj in d_bucket.objects.all() if re.search(f"^{sample_folder}/",obj.key) and obj.key != f"{sample_folder}/" ]

for file in download_files:
    obj = d_bucket.Object(file)
    file_path = os.path.join(sample_file_path,os.path.basename(file))
    with open(file_path, 'wb') as data:
        obj.download_fileobj(data)
# chek if files are downloaded
os.system(f"ls {sample_file_path}")
os.system("df -h")

# Run command
cmd = f"{cellranger} count --id={sample_id} --fastqs={sample_file_path} --transcriptome={ref_file} --localcores={core} --localmem={memory} --expect-cells={expect_cells}"
os.system(f"echo {cmd}")
os.system(cmd)

# Upload output files
output_folder_path = os.path.join(os.getcwd(),sample_id)
files = os.listdir(output_folder_path)

## Upload function
def upload_obj(s3_resource,bucket_name,path,key):
    if os.path.isdir(path):
        for file in os.listdir(path):
            upload_obj(s3_resource,bucket_name,os.path.join(path,file),os.path.join(key,file)) 
        return
    obj = s3_resource.Bucket(bucket_name).Object(key)
    with open(path, 'rb') as data:
        obj.upload_fileobj(data)
    return

## Upload log
if "_log" in files:
    obj_key = os.path.join(sample_id,"_log")
    obj_path = os.path.join(os.path.join(os.getcwd(),sample_id),"_log")
    upload_obj(s3_resource,upload_bucket,obj_path,obj_key)

## Upload outs
if "outs" in files:
    outs_path = os.path.join(output_folder_path,"outs")
    outs_files = os.listdir(outs_path)
    outs_key = os.path.join(sample_id,"outs")
    for file in outs_files:
        if file != "analysis":
            file_path = os.path.join(outs_path,file)
            file_key = os.path.join(outs_key,file)
            upload_obj(s3_resource,upload_bucket,file_path,file_key)
            
## Upload metrics_summary_json
json_file = "metrics_summary_json.json"
counter_path = os.path.join(output_folder_path,"SC_RNA_COUNTER_CS")
for dirpath, dirnames, filenames in os.walk(counter_path):
    for file in filenames:
        if file == json_file:
            json_path = os.path.join(os.path.join(output_folder_path,os.path.join(dirpath)),file)
            json_key = os.path.join(sample_id,json_file)
            upload_obj(s3_resource,upload_bucket,json_path,json_key)

# Clean up
os.system("df -h")
os.system(f"rm -rf {os.path.join(os.getcwd(),sample_id)}")
os.system(f"rm -rf {sample_file_path}")
os.system("df -h")