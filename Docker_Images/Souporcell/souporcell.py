import os
import subprocess
import sys

# Env variables
sample_id = os.environ['sample_id']
download_bucket = os.environ['download_bucket']
upload_bucket = os.environ['upload_bucket']
threads = os.environ['threads']  # 4
num_clusters = os.environ['num_clusters']  # 4

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


# Find file path
download_path = os.path.join(mnt_dir, sample_id)
output_dir = os.path.join(mnt_dir, f"{sample_id}_SPC")
fasta_path = os.path.join(home_dir, os.path.join("fasta", "genome.fa"))

# Download files
cmd = f"aws s3 sync s3://{download_bucket}/{sample_id} {download_path}"
run_command(cmd)
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
            os.system(f"echo {cmd}")
            os.system(cmd)
            barcode_path = os.path.join(dirpath, "barcodes.tsv")
        elif file == "barcodes.tsv":
            barcode_path = os.path.join(dirpath, file)

# Run main command
cmd = f"souporcell_pipeline.py -i {bamfile_path} -b {barcode_path} -f {fasta_path} -t {threads} -o {output_dir} -k {num_clusters}"
run_command(cmd)

# Upload output files
subprocess.run("df -h", shell=True)
cmd = f"aws s3 sync {output_dir} s3://{upload_bucket}/{sample_id}"
run_command(cmd)

# Clean up
subprocess.run(f"rm -rf {output_dir}", shell=True)
subprocess.run(f"rm -rf {download_path}", shell=True)
subprocess.run("df -h", shell=True)
