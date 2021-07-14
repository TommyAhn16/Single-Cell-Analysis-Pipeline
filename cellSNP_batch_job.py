import os
import boto3

# Variables
download_bucket = "cellranger-result-bucket"
upload_bucket = "cellsnp-result"
job_que = "arn:aws:batch:ap-northeast-2:901858906361:job-queue/CellSNP_On_Demand"
job_def = "arn:aws:batch:ap-northeast-2:901858906361:job-definition/Cellsnp:3"
threads = "22" 
min_MAF = "0.1"
min_count = "100"

# AWS Client and Resource
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
batch_client = boto3.client('batch')

# Get samples to run
# files = s3_resource.Bucket(download_bucket).objects.all()
# finished_samples = set([os.path.dirname(file.key) for file in s3_resource.Bucket(upload_bucket).objects.all()])
# samples_to_run = set([os.path.dirname(file.key) for file in s3_resource.Bucket(download_bucket).objects.all() if os.path.dirname(file.key) not in finished_samples])
# print(f"Samples to run: {samples_to_run}")
samples_to_run = ["21_00776_LI_SING","21_00780_LI_SING","21_00784_LI_SING","21_00788_LI_SING","21_00858_LI_SING","21_00864_LI_SING","21_00866_LI_SING","21_00871_LI_SING","21_00875_LI_SING",'21_00876_LI_SING','21_00884_LI_SING','21_00889_LI_SING','21_00899_LI_SING','21_00913_LI_SING']



for sample in samples_to_run:
    env_variables = {'sample_id':sample,'download_bucket':download_bucket,'upload_bucket':upload_bucket,'threads':threads,'min_MAF':min_MAF,'min_count':min_count}
    response = batch_client.submit_job(
                jobName= sample,
                jobQueue= job_que,
                jobDefinition= job_def,
                containerOverrides={'environment': [{'name':key,'value':env_variables[key]} for key in env_variables],})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f"{sample} job submitted")
    else:
        print(f"Failed to submit {sample} job")