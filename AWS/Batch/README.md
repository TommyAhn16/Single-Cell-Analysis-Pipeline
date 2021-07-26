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
- `securityGroupIds`, `subnets`, `securityGroupIds`, `ec2KeyPair` should be replaced with one's own
---
## Job Definitions
[AWS CLI Doc]()
---
## Job Queues
[AWS CLI Doc]()
---

