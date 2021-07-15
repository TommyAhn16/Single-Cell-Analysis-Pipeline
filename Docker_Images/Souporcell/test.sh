export sample_id=LI_SING
export download_bucket=cellranger-result-bucket
export upload_bucket=spc-result-bucket
export threads=4
export num_clusters=4
conda install -y -c conda-forge awscli
aws configure set aws_access_key_id AKIA5D6X22D42NHKFCDC
aws configure set aws_secret_access_key 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
aws configure set region ap-northeast-2
aws configure set output json