# Create AWS Batch components from AWS CLI
---
## Compute Environments
[AWS CLI Doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html)
### Command
```Bash
aws batch create-compute-environment --cli-input-json file://<json file>
```
### Example
```Bash
aws batch create-compute-environment --cli-input-json file://500GB_gp3_spot.json
```
### Notes
- Should have all [launch templates](../EC2/README.md) created before attempting to create compute environments
- `subnets`, `securityGroupIds`, `ec2KeyPair` should be replaced with one's own
---
## Job Definitions
[AWS CLI Doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html)
### Command
```Bash
aws batch register-job-definition --cli-input-json file://<json file>
```
### Example
```Bash
aws batch register-job-definition --cli-input-json file://cellranger.json
```
### Notes
- Replace `image` with one's own docker image in ECR
---
## Job Queues
[AWS CLI Doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html)
### Command
```Bash
aws batch create-job-queue --cli-input-json file://<json file>
```
### Example
```Bash
aws batch create-job-queue --cli-input-json file://cellranger.json
```
### Notes
- Should have all **compute environments** created before hand

---

