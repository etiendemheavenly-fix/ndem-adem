# Ndem-aDem Matrix Control Engine

A completely new microservices web workspace structured in a dark matrix style. It runs entirely inside containerized top>

## Architecture Mapping
* **Frontend-Tier**: Container serving customized responsive structures routed across standard public interfaces.
* **Backend-Tier**: Hidden middleware processing parameters via secure isolated network ports.

## Automated Manual Deployment Sequence
```bash
# 1. Spawn network mesh
docker network create ndem-network-mesh

# 2. Compile system targets
cd backend && docker build -t ndem-backend:v1 . && cd ..
cd frontend && docker build -t ndem-frontend:v1 . && cd ..

# 3. Instantiate container layers
docker run -d --name ndem-backend-service --network ndem-network-mesh ndem-backend:v1
docker run -d --name ndem-frontend-service --network ndem-network-mesh -p 8080:80 ndem-frontend:v1
```
# Ndem-aDem Matrix Control Engine

A completely new microservices web workspace structured in a dark matrix style. It runs entirely inside containerized topologies across separated communication profiles.

## Architecture Mapping
* **Frontend-Tier**: Container serving customized responsive structures routed across standard public interfaces.
* **Backend-Tier**: Hidden middleware processing parameters via secure isolated network ports.

## Automated Manual Deployment Sequence
```bash
# 1. Spawn network mesh
docker network create ndem-network-mesh

# 2. Compile system targets
cd backend && docker build -t ndem-backend:v1 . && cd ..
cd frontend && docker build -t ndem-frontend:v1 . && cd ..

# 3. Instantiate container layers
docker run -d --name ndem-backend-service --network ndem-network-mesh ndem-backend:v1
docker run -d --name ndem-frontend-service --network ndem-network-mesh -p 8080:80 ndem-frontend:v1
```
