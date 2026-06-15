# ECR Login Commands

Authenticate Docker to Amazon ECR.

## Local Machine

```bash
aws ecr get-login-password --region us-east-1 \
| docker login \
--username AWS \
--password-stdin <REPLACE_PASSWORD>.dkr.ecr.us-east-1.amazonaws.com
```

## EC2 Instance

```bash
aws ecr get-login-password --region us-east-1 \
| docker login \
--username AWS \
--password-stdin <REPLACE_PASSWORD>.dkr.ecr.us-east-1.amazonaws.com
```