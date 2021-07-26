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
    AWS_KEY = ""
    AWS_SECRET_KEY = ""
    REGION = ""
    n_donor = ""

    for env in env_variables:
        if env["Name"] == "sample_id":
            sample_id = env["Value"]
        elif env["Name"] == "min_MAF":
            min_MAF = env["Value"]
        elif env["Name"] == "min_count":
            min_count = env["Value"]
        elif env["Name"] == "AWS_KEY":
            AWS_KEY = env["Value"]
        elif env["Name"] == "AWS_SECRET_KEY":
            AWS_SECRET_KEY = env["Value"]
        elif env["Name"] == "REGION":
            REGION = env["Value"]
        elif env["Name"] == "n_donor":
            n_donor = env["Value"]
    
    return {
    "sample_id": sample_id,
    "min_MAF": min_MAF,
    "min_count": min_count,
    "download_bucket":download_bucket,
    "upload_bucket":upload_bucket,
    "threads":threads,
    "n_donor": n_donor,
    "AWS_KEY": AWS_KEY,
    "AWS_SECRET_KEY": AWS_SECRET_KEY,
    "REGION" : REGION
    }