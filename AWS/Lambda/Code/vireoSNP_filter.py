def lambda_handler(event, context):
    # Fixed Variables
    download_bucket = "cellsnp-original-result"
    upload_bucket = "vireosnp-result"
    

    # Variables from input
    env_variables = event["Container"]["Environment"]
    sample_id = ""
    n_donor = ""
    AWS_KEY = ""
    AWS_SECRET_KEY = ""
    REGION = ""

    for env in env_variables:
        if env["Name"] == "sample_id":
            sample_id = env["Value"]
        elif env["Name"] == "n_donor":
            n_donor = env["Value"]
        elif env["Name"] == "AWS_KEY":
            AWS_KEY = env["Value"]
        elif env["Name"] == "AWS_SECRET_KEY":
            AWS_SECRET_KEY = env["Value"]
        elif env["Name"] == "REGION":
            REGION = env["Value"]

    return {
    "sample_id": sample_id,
    "n_donor": n_donor,
    "download_bucket":download_bucket,
    "upload_bucket":upload_bucket,
    "AWS_KEY": AWS_KEY,
    "AWS_SECRET_KEY": AWS_SECRET_KEY,
    "REGION" : REGION
    }