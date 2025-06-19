| Component         | Choice                 | Rationale                                  |
| ----------------- | ---------------------- | ------------------------------------------ |
| **Auth**          | Firebase Auth (Google) | Dead-simple, Google-backed, works w/ React |
| **Frontend**      | React + TypeScript     | Vite + React Router + Tailwind             |
| **Backend**       | FastAPI                | Lightweight, async-native, dev-first       |
| **Infra**         | GCP + Cloud Run        | Serverless containers + simple scaling     |
| **DB**            | AlloyDB (Postgres)     | GCP-native, Postgres compatibility         |
| **Vector Store**  | Qdrant (Docker)        | Easy self-hosting, production-ready        |
| **Monitoring**    | Prometheus + Grafana   | Container/infra-level observability        |
| **Feature Flags** | Statsig                | React + Python SDK support, free tier ok   |
