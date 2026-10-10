# Doctor Appointment System

A lightweight starter project for a doctor appointment booking system.

## Project structure

```text
doctor-appointment-system/
├── app/
│   ├── __init__.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/
```

## Prerequisites

- Python 3.11+
- pip

## Setup

```bash
cd doctor-appointment-system
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run the app

```bash
uvicorn app.main:app --reload
```

Then open the API docs at:

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Run tests

```bash
pytest -q
```

## Notes

This is a starter scaffold. You can extend it with patient, doctor, appointment, authentication, and database models as your app grows.
