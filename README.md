# Payment API Simulator using FastAPI

[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/arshinkazi/payment-api-simulator)

**Live Demo:** [https://payment-api-simulator.onrender.com/docs](https://payment-api-simulator.onrender.com/docs)

A sandbox API to simulate card-based payment transactions. Built with **Python FastAPI**, it allows developers and students to test payments safely without connecting to real banking networks.

## Features

* **Payment Authorization (`/pay`)** – Approves or declines transactions based on card validity and balance.
* **Refund Processing (`/refund`)** – Refund amounts to accounts.
* **Card Validation** – Uses the Luhn algorithm to ensure only valid card numbers are processed.
* **Interactive Documentation** – Auto-generated via Swagger UI (`/docs`) and ReDoc (`/redoc`).
* **Friendly Root Route (`/`)** – Displays a welcome message with links to documentation.
* **In-Memory Storage** – Simple Python dict for accounts and balances.

## Quick Start

Clone the repository and navigate into it:
`git clone https://github.com/<your-username>/payment-api-simulator.git`
`cd payment-api-simulator`

Create and activate a virtual environment:

**Windows:**
`python -m venv venv`
`venv\Scripts\activate`

**Linux/Mac:**
`python -m venv venv`
`source venv/bin/activate`

Install dependencies:
`pip install -r requirements.txt`

Run the API locally:
`uvicorn main:app --reload`

* Root URL: `http://127.0.0.1:8000/`
* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

## Sample Requests

**Approve Payment:**
`curl -X POST "http://127.0.0.1:8000/pay?cardNumber=4111111111111111&amount=200&currency=USD"`

**Decline Payment (Insufficient Funds):**
`curl -X POST "http://127.0.0.1:8000/pay?cardNumber=5555555555554444&amount=9999&currency=USD"`

**Refund Payment:**
`curl -X POST "http://127.0.0.1:8000/refund?cardNumber=4111111111111111&amount=50"`

## Applications

* Classroom or lab sandbox for teaching payment flows
* Local integration testing without external dependencies
* Interview/demo artifact showing backend competency in fintech

## Future Scope

* Database persistence (SQLite/PostgreSQL)
* Authentication & Authorization (JWT)
* Docker containerization for easy deployment
* Frontend dashboard to test payments and visualize balances

## License

Open-source and free to use.
