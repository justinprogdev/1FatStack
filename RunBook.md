# 1FatStack: Service Overview

This document lists the major components of your stack, with accessible URLs and port mappings.

---

## 🌐 Services

### 1. **Frontend (Vite + React)**
- **URL (Localhost):** [http://localhost:5173](http://localhost:5173)
- **Docker Service Name:** `1fatstack-frontend-1`
- **Port:** `5173`
- **Notes:** Vite dev server with HMR enabled.

---

### 2. **Backend API (FastAPI)**
- **URL (Localhost):** [http://localhost:8000](http://localhost:8000)
- **OpenAPI Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Docker Service Name:** `1fatstack-api-1`
- **Port:** `8000`
- **Notes:** Uvicorn is serving FastAPI on port `8000`.

---

### 3. **Vector Store (Qdrant)**
- **Dashboard URL:** [http://localhost:6333/dashboard](http://localhost:6333/dashboard)
- **Docker Service Name:** `1fatstack-vector-db-1`
- **Ports:**
  - **HTTP API:** `6333`
  - **gRPC API:** `6334`
- **Notes:** Accessible via REST or gRPC. Used for semantic search.

---

### 4. **PostgreSQL Database**
- **Docker Service Name:** `1fatstack-db-1`
- **Port:** `5432`
- **Username:** `postgres` (default)
- **Notes:** Backend storage for your structured app data.

---

## 🔁 Internal Networking (Docker Compose)
These services are networked internally under `1fatstack_default`, enabling resolution via container names:
- FastAPI backend connects to Qdrant at `http://vector-db:6333`
- API connects to DB via `postgres://postgres@db:5432`

---

## 🐳 Docker Compose Commands

Start/rebuild the stack:
```bash
docker compose up --build