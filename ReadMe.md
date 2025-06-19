# 1FatStack: Service Overview

#### This is merely a guide I followed to build 1FatStack   
#### I recommend you go here and just run it <a href="https://github.com/justinprogdev/1FatStack/blob/main/RunBook.md">RunBook</a> 🤖




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
```
docker compose up --build
```
---

## ✅ JD-Inspired Stack Plan (Refined)

| Component         | Choice                 | Rationale                                  |
| ----------------- | ---------------------- | ------------------------------------------ |
| **Auth**          | Firebase Auth (Google) | Fast setup, works great with React         |
| **Frontend**      | React + TypeScript     | Vite + Router + Tailwind                   |
| **Backend**       | FastAPI                | Async, clean, Python-native                |
| **Infra**         | GCP + Cloud Run        | Scalable, cheap to start, full-stack-ready |
| **DB**            | AlloyDB (Postgres)     | GCP-native Postgres                        |
| **Vector Store**  | Qdrant (Docker)        | Simple, robust, local or hosted            |
| **Monitoring**    | Prometheus + Grafana   | Battle-tested observability stack          |
| **Feature Flags** | Statsig                | Modern, integrates well across stack       |

---

## 🔧 Step-by-Step Build Order (Fixed and Streamlined)

---

### **1. React Frontend Scaffold (With Firebase Install After)**

```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
npm install react-router-dom
npm install firebase
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Set up:

* `tailwind.config.js`
* Add Tailwind to `index.css`
* Configure `firebase.ts` with `initializeApp(...)`

---

### **2. Firebase Setup (After Frontend Exists)**

* Go to [Firebase Console](https://console.firebase.google.com/)
* Create a new project
* Enable **Authentication → Sign-in method → Google**
* Go to **Project Settings** → get `apiKey`, `authDomain`, etc.
* Create `src/firebase.ts`:

  ```ts
  import { initializeApp } from "firebase/app";
  import { getAuth, GoogleAuthProvider } from "firebase/auth";

  const firebaseConfig = {
    apiKey: "xxx",
    authDomain: "xxx.firebaseapp.com",
    projectId: "xxx",
  };

  const app = initializeApp(firebaseConfig);
  export const auth = getAuth(app);
  export const provider = new GoogleAuthProvider();
  ```

---

### **3. Backend API Setup (FastAPI)**

```bash
mkdir app && cd app
python -m venv venv && source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
pip install fastapi[all] uvicorn psycopg2-binary
```

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello world"}
```

---

### **4. Docker Compose for Dev**

You’ll run:

* FastAPI backend
* React frontend
* Postgres DB
* Optional: Qdrant vector store

Let me know and I’ll generate:

* `docker-compose.yml`
* `Dockerfile` for React + FastAPI

---

### **5. Qdrant Vector Store Setup**

In `docker-compose.yml`:

```yaml
vector-db:
  image: qdrant/qdrant
  ports:
    - "6333:6333"
```

In FastAPI:

```bash
pip install qdrant-client sentence-transformers
```

Create `services/embedding.py` with Qdrant wrapper class.

---

### **6. GCP Infrastructure Plan**

Use GCP services:

* Cloud Run: container deploy for API & optionally frontend
* Cloud SQL (AlloyDB): managed PostgreSQL
* Artifact Registry: store container builds
* Cloud Build or GitHub Actions: CI/CD

---

### **7. Monitoring: Prometheus + Grafana**

Use Docker locally:

* `prometheus.yml` config
* Mount metrics from FastAPI using:

  ```bash
  pip install prometheus-fastapi-instrumentator
  ```

Expose metrics at `/metrics`.

---

### **8. Feature Flags with Statsig**

* [Install React SDK](https://docs.statsig.com/client/javascript)
* [Install Python SDK](https://docs.statsig.com/server/python)
* Use:

  ```ts
  statsig.checkGate("new-feature")
  ```

---

## ✅ Ready to Generate Files?

Choose what you want dropped in next:

* `docker-compose.yml`
* `Dockerfile.api` / `Dockerfile.frontend`
* `firebase.ts` auth handler
* Qdrant integration
* Prometheus starter config

Let’s build it.
