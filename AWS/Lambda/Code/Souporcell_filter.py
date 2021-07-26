def lambda_handler(event, context):
    # Fixed Variables
    download_bucket = "cellranger-result-bucket"
    upload_bucket = "spc-result-bucket"

    # Variables from input
    env_variables = event["Container"]["Environment"]
    sample_id = ""
    num_clusters = ""
    threads = ""
    AWS_KEY = ""
    AWS_SECRET_KEY = ""
    REGION = ""

    for env in env_variables:
        if env["Name"] == "sample_id":
            sample_id = env["Value"]
        elif env["Name"] == "num_clusters":
            num_clusters = env["Value"]
        elif env["Name"] == "SPC_threads":
            threads = env["Value"]
        elif env["Name"] == "AWS_KEY":
            AWS_KEY = env["Value"]
        elif env["Name"] == "AWS_SECRET_KEY":
            AWS_SECRET_KEY = env["Value"]
        elif env["Name"] == "REGION":
            REGION = env["Value"]

    return {
        "sample_id": sample_id,
        "download_bucket": download_bucket,
        "upload_bucket": upload_bucket,
        "threads": threads,
        "num_clusters": num_clusters,
        "AWS_KEY": AWS_KEY,
        "AWS_SECRET_KEY": AWS_SECRET_KEY,
        "REGION" : REGION
        
    }
