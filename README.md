# RecordKeeper

RecordKeeper is a Django-based record-keeping system for small shops and operators to manage customers, application approvals, government fee payments, and revenue tracking.

---

## Master Branch has Actual Code

## Features

- Customer management (detailed customer & application records)  
- Application workflow with approval/pending states and operator tracking  
- Government fee tracking and balance calculations  
- Revenue reporting (past 30 days)  
- User authentication and multi-user/operator support  
- Historical records for audits and re-verification

---

## Prerequisites

- Python 3.8+  
- pip  
- (Optional) virtualenv or venv for an isolated environment

---

## Quick Setup

1. Clone the repository
```bash
git clone https://github.com/Kaditya67/RecordKeeper.git
cd RecordKeeper
```

2. Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Open the app
Visit http://127.0.0.1:8000 in your browser.

---

## Configuration Notes

- Use environment variables or a `.env` file to store sensitive settings (e.g., SECRET_KEY, DEBUG, database credentials).  
- For production, use a proper WSGI server and configure static files, allowed hosts, and secure settings.

---

## Usage Overview

- Login with the superuser or operator account.  
- Add and manage customers via the dashboard.  
- View and process application approvals.  
- Track government fee payments and balances.  
- Generate revenue reports (30-day view) and review historical records for audits.

---

## Project Structure (high level)

- services/models.py — data models for customers, applications, fees, and approvals  
- services/views.py — views for records, revenue reporting, authentication, approvals  
- templates/ — HTML templates: login, approval, revenue report, confirmations, history  
- static/ — static assets (CSS, JS, images)  
- manage.py — Django management script

---

## Contributing

- Fork the repo, create a feature branch, open a pull request.  
- Include tests where applicable and keep changes small and focused.

---

## License

This project is released under the MIT License — see the LICENSE file for details.
