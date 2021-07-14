import os
import boto3

sample_id = os.environ['sample_id']
download_bucket = os.environ['download_bucket']
upload_bucket = os.environ['upload_bucket']
n_donor = os.environ['n_donor']

# Download files from CellSNP result
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} ./{sample_id}_cellSNP"
os.system(f"echo {cmd}")
os.system(cmd)

# Run command
cell_snp_path = os.path.join(os.getcwd(), f"{sample_id}_cellSNP")
output_path = os.path.join(os.getcwd(), f"{sample_id}")
cmd = f"vireo -c {cell_snp_path} -N {n_donor} -o {output_path}"
os.system(f"echo {cmd}")
os.system(cmd)

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


output_key = os.path.basename(output_path)
upload_obj(s3_resource, upload_bucket, output_path, output_key)

# Clean up
os.system("df -h")
os.system(f"rm -rf {output_path}")
os.system(f"rm -rf {cell_snp_path}")
os.system("df -h")
