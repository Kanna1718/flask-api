# Flask GitOps API

A lightweight, modern Python Flask API and frontend dashboard tailored for Kubernetes and ArgoCD GitOps practices.

## Features

- **Web Dashboard**: Modern, responsive frontend displaying running pod hostname, active version, and environment.
- **GitOps-Friendly**: Live endpoint testing allowing you to observe rolling updates and hostname changes in real-time.
- **Liveness & Readiness**: Health check endpoint ready for Kubernetes probes (`/health`, `/api/health`).
- **RESTful Endpoints**:
  - `GET /` - UI dashboard
  - `GET /health` or `GET /api/health` - Health status probe
  - `GET /api/info` - Hostname, version, environment, timestamp metadata
  - `GET /api/items` - List sample resources
  - `POST /api/items` - Add new resource

## Local Development

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## Docker

### Build Image
```bash
docker build -t flask-api:latest .
```

### Run Container
```bash
docker run -p 5000:5000 flask-api:latest
```

## Environment Variables

| Variable | Description | Default |
| --- | --- | --- |
| `PORT` | Listening port for the application | `5000` |
| `APP_VERSION` | Application version tag displayed on UI | `v1.0.0` |
| `APP_ENV` | Environment identifier (e.g., dev, staging, production) | `production` |
