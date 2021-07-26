# Create Lambda Functions with AWS CLI
[AWS CLI Doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html)
## Steps
1. zip all Python codes in [Code](./Code) directory
- Example: 
```bash
$ zip cellSNP_filter.zip cellSNP_filter.py
```
2. Run each AWS CLI commands found below
- Note: `role` should be of one's own
## Commands
### cellSNP_filter
```bash
$ aws lambda create-function \
    --function-name cellSNP_filter \
    --runtime python3.7 \
    --zip-file fileb://cellSNP_filter.zip \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::901858906361:role/lambda_role_for_stepfunction
```
### vireoSNP_filter
```bash
$ aws lambda create-function \
    --function-name vireoSNP_filter \
    --runtime python3.7 \
    --zip-file fileb://vireoSNP_filter.zip \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::901858906361:role/lambda_role_for_stepfunction
```
### Souporcell_filter
```bash
$ aws lambda create-function \
    --function-name Souporcell_filter \
    --runtime python3.7 \
    --zip-file fileb://Souporcell_filter.zip \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::901858906361:role/lambda_role_for_stepfunction
```