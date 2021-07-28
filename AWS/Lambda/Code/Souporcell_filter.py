def lambda_handler(event, context):
    # Variables from input
    env_variables = event["Container"]["Environment"]
    # Shared
    SAMPLE_ID = ""
    AWS_KEY = ""
    AWS_SECRET_KEY = ""
    REGION = ""
    # Unique
    NUM_CLUSTERS = ""
    THREADS = ""
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
        elif env["Name"] == "CR_UPLOAD_BUCKET":
            DOWNLOAD_BUCKET = env["Value"]
        elif env["Name"] == "SPC_UPLOAD_BUCKET":
            UPLOAD_BUCKET = env["Value"]
        elif env["Name"] == "SPC_THREADS":
            THREADS = env["Value"]
        elif env["Name"] == "SPC_NUM_CLUSTERS":
            NUM_CLUSTERS = env["Value"]

    return {
        "SAMPLE_ID": SAMPLE_ID,
        "AWS_KEY":  AWS_KEY,
        "AWS_SECRET_KEY": AWS_SECRET_KEY,
        "REGION": REGION,
        "THREADS": THREADS,
        "DOWNLOAD_BUCKET": DOWNLOAD_BUCKET,
        "UPLOAD_BUCKET": UPLOAD_BUCKET,
        "NUM_CLUSTERS": NUM_CLUSTERS,
    }
