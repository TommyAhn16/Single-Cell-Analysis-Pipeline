def lambda_handler(event, context):
    # Variables from input
    env_variables = event["Container"]["Environment"]
    # Shared
    SAMPLE_ID = ""
    AWS_KEY = ""
    AWS_SECRET_KEY = ""
    REGION = ""
    # Unique
    N_DONOR = ""
    DOWNLOAD_BUCKET = ""
    UPLOAD_BUCKET = ""

    for env in env_variables:
        if env["Name"] == "SAMPLE_ID":
            SAMPLE_ID = env["Value"]
        elif env["Name"] == "AWS_KEY":
            AWS_KEY = env["Value"]
        elif env["Name"] == "AWS_SECRET_KEY":
            AWS_SECRET_KEY = env["Value"]
        elif env["Name"] == "REGION":
            REGION = env["Value"]
        elif env["Name"] == "UPLOAD_BUCKET":
            DOWNLOAD_BUCKET = env["Value"]
        elif env["Name"] == "VS_UPLOAD_BUCKET":
            UPLOAD_BUCKET = env["Value"]
        elif env["Name"] == "VS_N_DONOR":
            N_DONOR = env["Value"]

    return {
        "SAMPLE_ID": SAMPLE_ID,
        "AWS_KEY":  AWS_KEY,
        "AWS_SECRET_KEY": AWS_SECRET_KEY,
        "REGION": REGION,
        "DOWNLOAD_BUCKET": DOWNLOAD_BUCKET,
        "UPLOAD_BUCKET": UPLOAD_BUCKET,
        "N_DONOR": N_DONOR,
    }
