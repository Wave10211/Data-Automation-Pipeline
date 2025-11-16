Data Automation Pipeline

End-to-end data ingestion pipeline — stable, 
modular and production-ready scaffold for collecting JSON data
 from public APIs, transforming it and persisting it to SQLite.

This repository is a learning & portfolio project that demonstrates
 full lifecycle engineering:
- API integration (requests)
- Data validation & error handling
- Persistence layer using SQLAlchemy + SQLite

- CLI entrypoint and modular project layout
- CI pipeline for tests and linting (suggested)

---

 Highlights / Features
- Lightweight, modular architecture (`backend/`, `frontend/`, `data/`)
- Robust HTTP layer with error handling and fallback
- Extensible: add email notifications, dashboards (PyQt),
  or orchestration (Airflow/Prefect)
- Ready for containerization and CI/CD

---

 Tech Stack
- Python 3.10+    
- requests (HTTP client)  
- SQLAlchemy (ORM)  
- SQLite (local storage)  

---

 Quick start (development)

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/Data Automation Pipeline.git
   cd Data Automation Pipeline


-CREATE + ACTIVATE virtual environment

python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows cmd
.\.venv\Scripts\activate.bat
# mac / linux
source .venv/bin/activate

-INSTALL DEPENDENCIES

pip install -r requirements.txt

-RUN THE PIPELINE

python -m frontend.cli

-STRUCTURE

data-automation-pipeline/
├─ backend/
│  ├─ api/           # HTTP clients / fetchers
│  ├─ db/            # SQLAlchemy models & database bootstrap
│  └─ services/      # business logic (email, export, etc.)
├─ frontend/
│  └─ cli.py         # entrypoint: python -m frontend.cli
├─ data/
│  └─ pipeline.db    # sqlite database (gitignored)
├─ tests/            # unit tests
├─ requirements.txt
└─ README.md

Contact / Author

Munteanu Angela-munteanuangela21@yahoo.com