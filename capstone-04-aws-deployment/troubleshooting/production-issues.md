# Production Troubleshooting Notes

## Issue 1: ECR Authentication Failed

### Error

```text
push access denied
no basic auth credentials
EOF
```

### Resolution

- Verified AWS CLI credentials.
- Re-authenticated Docker using ECR login command.
- Verified correct ECR URI.

---

## Issue 2: Internal Server Error

### Error

```text
500 Internal Server Error
```

### Root Cause

Flask application expected Redis to be available.

Locally:

Flask + Redis worked through Docker Compose.

On EC2:

Only Flask was deployed.

Redis dependency was missing.

### Investigation

```bash
docker logs visitor-counter
```

Observed:

```text
redis.exceptions.ConnectionError:
Error -2 connecting to redis:6379.
Name or service not known.
```

### Resolution

Deployed Redis alongside Flask using Docker Compose.

---

## Biggest Lesson

A running container does not guarantee a healthy application.

Always inspect logs and verify application dependencies.