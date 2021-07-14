import boto3
import os
# Env variables
sample_id = os.environ['sample_id']
download_bucket = os.environ['download_bucket']
upload_bucket = os.environ['upload_bucket']
threads = os.environ['threads'] # 22
min_MAF = os.environ['min_MAF'] #  0.1
min_count = os.environ['min_count'] # 100

# Variables
home_dir = "/home/ec2-user"
mnt_dir = "/home/ec2-user/vol_mnt"

# File directory
download_path = os.path.join(mnt_dir,sample_id)
outs_path = os.path.join(download_path,"outs")
bamfile_path = os.path.join(outs_path,"possorted_genome_bam.bam")
barcode_path = os.path.join(os.path.join(outs_path,"filtered_feature_bc_matrix"),"barcodes.tsv.gz")
output_dir = os.path.join(mnt_dir,f"{sample_id}_cellSNP")

# Download files
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} {download_path}"
os.system(f"echo {cmd}")
os.system(cmd)
os.system("df -h")

# Decompress barcode
cmd = f"gunzip {barcode_path}"
os.system(f"echo {cmd}")
os.system(cmd)
barcode_path = os.path.join(os.path.join(outs_path,"filtered_feature_bc_matrix"),"barcodes.tsv")

# Run command
cmd = f"cellsnp-lite -s {bamfile_path} -b {barcode_path} -O {output_dir} -p {threads} --minMAF {min_MAF} --minCOUNT {min_count}"
os.system(f"echo {cmd}")
os.system(cmd)

# Upload output files
s3_resource = boto3.resource('s3')
## Upload function
def upload_obj(s3_resource,bucket_name,path,key):
    if os.path.isdir(path):
        for file in os.listdir(path):
            upload_obj(s3_resource,bucket_name,os.path.join(path,file),os.path.join(key,file))
        return
    obj = s3_resource.Bucket(bucket_name).Object(key)
    with open(path, 'rb') as data:
        obj.upload_fileobj(data)
    print(f"{key} uploaded")
    return

output_key = os.path.join(sample_id,os.path.basename(output_dir))
upload_obj(s3_resource,upload_bucket,output_dir,output_key)

# Clean up
os.system("df -h")
os.system(f"rm -rf {download_path}")
os.system(f"rm -rf {output_dir}")
os.system("df -h")

