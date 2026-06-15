# EC2 Docker Setup Commands

## Update Packages

```bash
sudo dnf update -y
```

## Install Docker

```bash
sudo dnf install docker -y
```

## Start Docker

```bash
sudo systemctl start docker
```

## Enable Docker on Boot

```bash
sudo systemctl enable docker
```

## Add ec2-user to Docker Group

```bash
sudo usermod -aG docker ec2-user
```

## Verify Docker

```bash
docker run hello-world
```