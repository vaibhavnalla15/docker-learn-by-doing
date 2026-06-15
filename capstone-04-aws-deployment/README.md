# 🚀 Capstone 04: Deploy a Multi-Container Docker Application on AWS

## 📌 Project Overview

In this capstone, I deployed a Containerized Flask Visitor Counter application backed by Redis onto AWS.

The application was first containerized locally, pushed to Amazon Elastic Container Registry (ECR), and then deployed on an Amazon EC2 instance using Docker Compose.

Unlike simple container deployments, this project involved troubleshooting real production-style issues, understanding service dependencies, and deploying a complete multi-container application in the cloud.

---

## 🎯 Project Goal

The objective of this capstone was to understand how Docker applications move from a developer laptop to AWS infrastructure.

This project bridges the gap between local Docker development and AWS container orchestration services such as Amazon ECS.

---

## 🏗️ Architecture

```text
Developer Laptop
       │
       ▼
Docker Image
       │
       ▼
Amazon ECR
       │
       ▼
Amazon EC2
       │
       ▼
Docker Compose
 ┌───────────────┐
 │ Flask Web App │
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │ Redis Server  │
 └───────┬───────┘
         │
         ▼
 Docker Volume
         │
         ▼
 Persistent Visitor Count
```

---

## 🛠 Technologies Used

* Docker
* Docker Compose
* Python
* Flask
* Redis
* Amazon ECR
* Amazon EC2
* Amazon Linux 2023
* AWS CLI
* SSH

---

## 📂 Project Workflow

### 1. Build Docker Image Locally

* Built the Flask Visitor Counter image.
* Verified it worked locally.

---

### 2. Create Amazon ECR Repository

Created a private ECR repository:

```
visitor-counter
```

Configured:

* Private repository
* Scan on Push enabled
* Default encryption

---

### 3. Authenticate Docker to ECR

Authenticated Docker Desktop using AWS credentials.

```text
Docker Desktop
↓
AWS Authentication
↓
Amazon ECR Access
```

---

### 4. Push Docker Image to ECR

Tagged and pushed the local image.

```text
Local Docker Image
↓
Amazon ECR
```

---

### 5. Launch Amazon EC2

Provisioned an EC2 instance using:

* Amazon Linux 2023
* t3.micro (Free Tier)
* SSH access
* HTTP access

---

### 6. Connect Using SSH

Connected securely using a PEM key.

```text
Laptop
↓
SSH
↓
Amazon EC2
```

---

### 7. Install Docker on EC2

Configured EC2 as a Docker host.

Installed:

* Docker Engine
* Docker Compose

Verified installation using:

```bash
docker run hello-world
```

---

### 8. Pull Images from ECR

Authenticated EC2 to ECR and pulled the application image.

```text
Amazon ECR
↓
Amazon EC2
```

---

### 9. Deploy Multi-Container Application

Used Docker Compose to deploy:

#### Flask Application

Responsibilities:

* Display visitor count
* Handle HTTP requests

#### Redis

Responsibilities:

* Store visitor count
* Provide persistent backend storage

---

### 10. Verify Persistence

Validated Docker volumes by:

Stopping the application:

```bash
docker compose down
```

Starting it again:

```bash
docker compose up -d
```

The visitor count remained intact.

---

## 🧠 Production Issue Encountered

### Problem

After deploying Flask on EC2, the browser returned:

```text
500 Internal Server Error
```

---

### Investigation

Checked container logs:

```bash
docker logs visitor-counter
```

Observed:

```text
redis.exceptions.ConnectionError:
Error -2 connecting to redis:6379.
Name or service not known.
```

---

### Root Cause

The Flask application expected Redis to exist.

Locally:

```text
Docker Compose
│
├── Flask
└── Redis
```

On EC2:

```text
EC2
└── Flask
```

Redis had not been deployed.

---

### Resolution

Deployed the complete stack using Docker Compose.

```text
EC2
│
├── Flask Container
└── Redis Container
```

Docker networking automatically resolved:

```text
redis
↓
Redis Container
```

The application recovered successfully.

---

## 🔍 Troubleshooting Journey

### ECR Authentication Errors

Encountered:

```text
no basic auth credentials
EOF
```

Resolved by:

* Re-authenticating Docker with ECR.
* Verifying AWS CLI credentials.
* Confirming ECR repository URI.

---

### Docker Compose Installation Issue

Encountered:

```text
No match for argument: docker-compose-plugin
```

Resolved by:

* Verifying Docker Compose availability.
* Using the existing Compose installation.

---

### Internal Server Error

Encountered:

```text
500 Internal Server Error
```

Resolved by:

* Inspecting application logs.
* Identifying missing Redis dependency.
* Deploying the full multi-container stack.

---

## 📚 Key Learnings

### Docker

* Building images
* Tagging images
* Running containers
* Docker networking
* Docker volumes

### AWS

* Amazon ECR
* Amazon EC2
* SSH access
* AWS CLI authentication

### Docker Compose

* Multi-container applications
* Service discovery
* Environment variables
* Persistent storage

### Troubleshooting

* Reading Docker logs
* Diagnosing dependency failures
* Distinguishing infrastructure issues from application issues
* Root cause analysis

---

## 💡 Biggest Lesson

A running container does not guarantee a healthy application.

```text
EC2 Running          ✅
Docker Running       ✅
Container Running    ✅
Application Healthy  ❌
```

Always verify application dependencies and inspect logs.

---

## 🎯 Outcome

Successfully deployed a production-style multi-container Flask and Redis application on AWS using Docker Compose, Amazon ECR, and Amazon EC2.

This project provided practical experience with container deployment, cloud infrastructure, persistent storage, and real-world troubleshooting.

---

## 🚀 Future Enhancements

* Deploy the same application on Amazon ECS.
* Automate deployments using GitHub Actions.
* Implement ECS Fargate.
* Add CloudWatch logging and monitoring.
* Introduce Application Load Balancer (ALB).
* Enable HTTPS using ACM.

```
```
