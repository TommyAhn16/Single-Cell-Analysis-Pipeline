import os
import boto3

# Variables
download_bucket = "cellranger-result-bucket"
prefix = "21_00889_LI_SING"
s3_resource = boto3.resource('s3')
# ## Upload metrics_summary_json
# json_file = "metrics_summary_json.json"
# counter_path = os.path.join(output_folder_path,"SC_RNA_COUNTER_CS")
# for dirpath, dirnames, filenames in os.walk(download_path):
#     for file in filenames:
#         if file == json_file:
#             json_path = os.path.join(os.path.join(output_folder_path,os.path.join(dirpath)),file)



objs = [obj.key for obj in s3_resource.Bucket(download_bucket).objects.all() if os.path.basename(obj.key) and os.path.dirname(obj.key) == prefix]
print(objs)