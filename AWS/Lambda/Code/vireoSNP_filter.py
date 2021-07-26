def lambda_handler(event, context):
    # Fixed Variables
    download_bucket = "cellsnp-original-result"
    upload_bucket = "vireosnp-result"

    # Variables from input
    env_variables = event["Container"]["Environment"]
    sample_id = ""
    n_donor = ""

    for env in env_variables:
        if env["Name"] == "sample_id":
            sample_id = env["Value"]
        elif env["Name"] == "n_donor":
            n_donor = env["Value"]

    return {
        "sample_id": sample_id,
        "n_donor": n_donor,
        "download_bucket": download_bucket,
        "upload_bucket": upload_bucket
    }
