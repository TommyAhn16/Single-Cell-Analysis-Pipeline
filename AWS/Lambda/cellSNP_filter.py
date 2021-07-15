def lambda_handler(event, context):
    # Fixed Variables
    download_bucket = "cellranger-result-bucket"
    upload_bucket = "cellsnp-original-result" 
    threads = "22"

    # Variables from input
    env_variables = event["Container"]["Environment"]
    sample_id = ""
    min_MAF = ""
    min_count = ""

    for env in env_variables:
        if env["Name"] == "sample_id":
            sample_id = env["Value"]
        elif env["Name"] == "min_MAF":
            min_MAF = env["Value"]
        elif env["Name"] == "min_count":
            min_count = env["Value"]
    
    return {
    "sample_id": sample_id,
    "min_MAF": min_MAF,
    "min_count": min_count,
    "download_bucket":download_bucket,
    "upload_bucket":upload_bucket,
    "threads":threads
    }