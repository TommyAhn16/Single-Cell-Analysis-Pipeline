import os
import boto3

# Variables
download_bucket = "cellranger-input-bucket"
upload_bucket = "cellranger-result-bucket"
job_que = "arn:aws:batch:ap-northeast-2:901858906361:job-queue/Cellranger_1TB"
job_def = "arn:aws:batch:ap-northeast-2:901858906361:job-definition/Cellranger_1TB:2"
core = "8" 
memory = "50"
expect_cells = "9000"

# AWS Client and Resource
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
batch_client = boto3.client('batch')

# Get samples to run
files = s3_resource.Bucket(download_bucket).objects.all()
finished_samples = set([os.path.dirname(file.key) for file in s3_resource.Bucket(upload_bucket).objects.all()])
samples_to_run = set([os.path.dirname(file.key) for file in s3_resource.Bucket(download_bucket).objects.all() if os.path.dirname(file.key) not in finished_samples])
print(f"Samples to run: {samples_to_run}")

for sample in samples_to_run:
    env_variables = {'sample_folder':sample,'download_bucket':download_bucket,'upload_bucket':upload_bucket,'sample_id':sample,'core':core,'memory':memory,'expect_cells':expect_cells}
    response = batch_client.submit_job(
                jobName= sample,
                jobQueue= job_que,
                jobDefinition= job_def,
                containerOverrides={'environment': [{'name':key,'value':env_variables[key]} for key in env_variables],})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f"{sample} job submitted")
    else:
        print(f"Failed to submit {sample} job")