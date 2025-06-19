# ***The Runbook***

# 1FatStack: Service Overview

This document lists the major components of the 1fatstack, with accessible URLs and port mappings.



## 🌐 Services

### 1. **Frontend (Vite + React)**
- **URL:** [http://localhost:5173](http://localhost:5173)
- **Docker Service:** `1fatstack-frontend-1`
- **Port:** `5173`
- **Notes:** Vite dev server with hot module reload (HMR).

---

### 2. **Backend API (FastAPI)**
- **URL:** [http://localhost:8000](http://localhost:8000)
- **OpenAPI Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Docker Service:** `1fatstack-api-1`
- **Port:** `8000`
- **Notes:** Served via Uvicorn. Prometheus metrics exposed at `/metrics`.

---

### 3. **Vector Store (Qdrant)**
- **Dashboard:** [http://localhost:6333/dashboard](http://localhost:6333/dashboard)
- **Docker Service:** `1fatstack-vector-db-1`
- **Ports:**
  - **HTTP API:** `6333`
  - **gRPC API:** `6334`
- **Notes:** Vector search for semantic note matching.

---

### 4. **PostgreSQL Database**
- **Docker Service:** `1fatstack-db-1`
- **Port:** `5432`
- **Username:** `postgres`
- **Notes:** Structured data store for FastAPI backend.

---

### 5. **Grafana**
- **URL:** [http://localhost:3000](http://localhost:3000)
- **Docker Service:** `1fatstack-grafana`
- **Port:** `3000`
- **Default Login:** `admin / admin`
- **Notes:** Visualizes metrics from Prometheus. Add Prometheus as a data source at `http://prometheus:9090`.

---

## 🔁 Internal Networking (Docker Compose)

These services resolve each other via internal names under the `1fatstack_default` Docker network:

- FastAPI connects to Qdrant at `http://vector-db:6333`
- FastAPI connects to PostgreSQL at `postgres://user:password@db:5432`

---

## 🐳 Docker Compose Commands

### Start/rebuild the stack:
```bash
docker compose up --build
````

### Tear down and clean volumes:

```bash
docker compose down -v
```

### Shell into API container:

```bash
docker exec -it 1fatstack-api-1 bash
```

