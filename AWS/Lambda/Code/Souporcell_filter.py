def lambda_handler(event, context):
    # Fixed Variables
    download_bucket = "cellranger-result-bucket"
    upload_bucket = "spc-result-bucket"

    # Variables from input
    env_variables = event["Container"]["Environment"]
    sample_id = ""
    num_clusters = ""
    threads = ""

    for env in env_variables:
        if env["Name"] == "sample_id":
            sample_id = env["Value"]
        elif env["Name"] == "num_clusters":
            num_clusters = env["Value"]
        elif env["Name"] == "SPC_threads":
            threads = env["Value"]

    return {
        "sample_id": sample_id,
        "download_bucket": download_bucket,
        "upload_bucket": upload_bucket,
        "threads": threads,
        "num_clusters": num_clusters
    }
