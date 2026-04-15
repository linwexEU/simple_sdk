# 📚 FastAPI Books Service

A modular and production-ready backend service built with **FastAPI**, following clean architecture principles. The project demonstrates structured layering (API → Services → Repositories), custom exception handling, dependency injection, and reusable utilities.

---

## 🚀 Features

* ⚡ FastAPI-based asynchronous API
* 🧩 Clean architecture (routers, services, repositories)
* 🔁 Reusable HTTP client with lifecycle management
* 🛑 Custom exception handling (service & external API errors)
* 📦 Pydantic schemas for validation
* 🧠 Centralized logging configuration
* 🔌 Dependency injection via FastAPI `Depends`
* 🗂️ Scalable project structure

---

## 📁 Project Structure

```
src/
│
├── api/
│   ├── routers/        # API endpoints (auth, books)
│   ├── services/       # Business logic
│   ├── depencencies.py # Dependency injection setup
│
├── repositories/       # Data access layer
│
├── schemas/            # Pydantic models
│
├── exceptions/
│   ├── handlers/       # Exception handlers (FastAPI layer)
│   ├── services/       # Service-level exceptions
│   ├── repositories/   # Repository-level exceptions
│   ├── http/           # External API exceptions
│
├── utils/
│   ├── config.py       # Configuration management
│   ├── http_client.py  # Async HTTP client wrapper
│   ├── logger.py       # Logging setup
│
└── main.py             # App entry point
```

---

## 🔧 Installation

Manual(Go to: http://127.0.0.1:8000/docs):
```bash
git clone <your-repo>
cd project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app # Before run, create and configure .env file
```

Docker(Go to: http://127.0.0.1:7777/docs):
```bash
docker compose -f ./docker/docker-compose.yml up # Before run, create and configure .env-docker file
```
