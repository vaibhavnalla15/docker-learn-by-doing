# Deployment Commands

## Pull Application Image

```bash
docker pull <img-ecr-url>
```

## Start Application

```bash
docker compose up -d
```

## Verify Running Containers

```bash
docker ps
```

## Stop Application

```bash
docker compose down
```

## Restart Application

```bash
docker compose up -d
```

## View Logs

```bash
docker logs visitor-counter
docker logs redis
```