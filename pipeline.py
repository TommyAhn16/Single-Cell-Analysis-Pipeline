import boto3
import os
import json
 
def start_state_machine(SFN_client,state_machine_arn:str,input:dict)->dict:
    """
    Start execution of a state machine with given input

    Parameters
    -------------------------------------------------------------------------------
    - SFN_client: AWS step functions client (e.g. boto3.client('stepfunctions'))
    - state_machine_arn: state machine arn within SFN
    - input: input to pass on to the state machine. Python dict type (e.g. {'key':'value'})
    -------------------------------------------------------------------------------
    
    Return
    -------------------------------------------------------------------------------
    Returns the response from starting the state machine (Python dict type)
    
    """
    response = SFN_client.start_execution(
                stateMachineArn=state_machine_arn,
                input=json.dumps(input)
                )
    return response
def run_type_1(SFN_client,state_machine_arn,input):
    """
    Cell Ranger -> cellSNP -> vireoSNP
                    -> Souporcell
    """
def run_type_2(SFN_client,state_machine_arn,input):
    """
    cellSNP -> vireoSNP
    
    input example:
    {
    "sample_id": "21_01101_LI_SING",
    "download_bucket": "cellranger-result-bucket",
    "upload_bucket": "cellsnp-original-result",
    "threads": "22",
    "min_MAF": "0.1",
    "min_count": "100",
    "n_donor": "4"}
    """
if __name__ == "__main__":
    aws_key_id = os.environ['AWS_KEY']
    aws_secret_key = os.environ['AWS_SECRET']
    SFN_client = boto3.client('stepfunctions',aws_access_key_id=aws_key_id,aws_secret_access_key=aws_secret_key)
    
    

