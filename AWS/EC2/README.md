# Create EC2 launch template from AWS CLI
[AWS CLI Doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template.html)
> EC2 launch template is needed to attach extra EBS volumes to EC2 instances initiated by AWS Batch job
## Command
```bash
aws ec2 create-launch-template \
  --launch-template-name <template name> \
  --launch-template-data file://<json file path>
```
## Example

```bash
aws ec2 create-launch-template \
  --launch-template-name 500GB_gp3 \
  --launch-template-data file://500GB_gp3.json
```
## Note
- `UserData` value in launch template data json file is a **Base64** encoding for:
```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/x-shellscript; charset="us-ascii"

#!/bin/bash
yum -y install util-linux
yum -y install xfsprogs 
mkdir /vol_mnt
mkfs -t xfs /dev/nvme1n1
mount /dev/nvme1n1 /vol_mnt

--==MYBOUNDARY==--
``` 