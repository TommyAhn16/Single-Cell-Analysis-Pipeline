def lambda_handler(event, context):
    # Variables from input
    env_variables = event["Container"]["Environment"]
    # Shared
    SAMPLE_ID = ""
    AWS_KEY = ""
    AWS_SECRET_KEY = ""
    REGION = ""
    # Unique
    MIN_MAF = ""
    MIN_COUNT = ""
    THREADS = ""
    DOWNLOAD_BUCKET = ""
    UPLOAD_BUCKET = ""
    VS_UPLOAD_BUCKET = ""
    VS_N_DONOR = ""

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
        elif env["Name"] == "CS_UPLOAD_BUCKET":
            UPLOAD_BUCKET = env["Value"]
        elif env["Name"] == "CS_THREADS":
            THREADS = env["Value"]
        elif env["Name"] == "CS_MIN_MAF":
            MIN_MAF = env["Value"]
        elif env["Name"] == "CS_MIN_COUNT":
            MIN_COUNT = env["Value"]
        elif env["Name"] == "VS_N_DONOR":
            VS_N_DONOR = env["Value"]

    return {
        "SAMPLE_ID": SAMPLE_ID,
        "AWS_KEY":  AWS_KEY,
        "AWS_SECRET_KEY": AWS_SECRET_KEY,
        "REGION": REGION,
        "MIN_MAF": MIN_MAF,
        "MIN_COUNT": MIN_COUNT,
        "THREADS": THREADS,
        "DOWNLOAD_BUCKET": DOWNLOAD_BUCKET,
        "UPLOAD_BUCKET": UPLOAD_BUCKET,
        "VS_UPLOAD_BUCKET": VS_UPLOAD_BUCKET,
        "VS_N_DONOR": VS_N_DONOR,
    }
