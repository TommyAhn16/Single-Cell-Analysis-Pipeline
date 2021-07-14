import os
# Env variables
sample_id = os.environ['sample_id']
download_bucket = os.environ['download_bucket']
upload_bucket = os.environ['upload_bucket']
threads = os.environ['threads']  # 22
min_MAF = os.environ['min_MAF']  # 0.1
min_count = os.environ['min_count']  # 100

# Variables
home_dir = "/home/ec2-user"
mnt_dir = "/home/ec2-user/vol_mnt"

# File directory
download_path = os.path.join(mnt_dir, sample_id)
output_dir = os.path.join(mnt_dir, f"{sample_id}_cellSNP")

# Download files
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} {download_path}"
os.system(f"echo {cmd}")
os.system(cmd)
os.system("df -h")

# Bam, barcode path
bamfile_path = ""
barcode_path = ""
for dirpath, dirnames, filenames in os.walk(download_path):
    for file in filenames:
        if file == "possorted_genome_bam.bam":
            bamfile_path = os.path.join(dirpath, file)
        elif file == "barcodes.tsv.gz":
            cmd = f"gunzip {os.path.join(dirpath,file)}"
            os.system(f"echo {cmd}")
            os.system(cmd)
            barcode_path = os.path.join(dirpath, "barcodes.tsv")
        elif file == "barcodes.tsv":
            barcode_path = os.path.join(dirpath, file)

# Run command
cmd = f"cellSNP -s {bamfile_path} -b {barcode_path} -O {output_dir} -p {threads} --minMAF {min_MAF} --minCOUNT {min_count}"
os.system(f"echo {cmd}")
os.system(cmd)

# Upload output files
cmd = f"aws s3 sync {output_dir} s3://{upload_bucket}/{sample_id}"
os.system(f"echo {cmd}")
os.system(cmd)

# Clean up
os.system("df -h")
os.system(f"rm -rf {download_path}")
os.system(f"rm -rf {output_dir}")
os.system("df -h")
