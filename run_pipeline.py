#!./env/bin/python3

import boto3
import json
from optparse import OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="input file in JSON format", metavar="FILE")
    parser.add_option("-a", "--state-machine-arn", dest="sm_arn",
                      help="AWS ARN of the pipeline state machine")
    (options, args) = parser.parse_args()

    with open(options.input, 'r') as data:
        sf_input = json.load(data)

    req_var = {'CS_UPLOAD_BUCKET', 'AWS_KEY', 'SPC_NUM_CLUSTERS', 'VS_N_DONOR', 'CR_DOWNLOAD_BUCKET', 'SPC_UPLOAD_BUCKET', 'CR_CORE', 'SAMPLE_ID', 'CS_MIN_MAF',
               'AWS_SECRET_KEY', 'CR_UPLOAD_BUCKET', 'VS_UPLOAD_BUCKET', 'SPC_THREADS', 'CR_MEMORY', 'CR_EXPECT_CELLS', 'CS_MIN_COUNT', 'CS_THREADS', 'REGION'}
    input_file_keys = set(sf_input.keys())

    if not req_var.issubset(input_file_keys):
        print("Missing one or more required variables")
        print(
            f"Missing variables: {', '.join(list(req_var - input_file_keys))}")
        return

    if not options.sm_arn:
        print("Missing [-a --state-machine-arn] option")
        print("Usage: run_pipeline.py -i <input json file> -a <state machine AWS ARN>")
        return

    SFN_client = boto3.client('stepfunctions')
    response = SFN_client.start_execution(
        stateMachineArn=options.sm_arn,
        input=json.dumps(sf_input)
    )
    print(response)
    return


if __name__ == "__main__":
    main()
