# RecordKeeper

A robust Django-based record and workflow management system designed for administrative offices, service centers, and small retail operators to track customer applications, government fee disbursements, approval stages, and monthly revenue metrics.

---

## 🌟 Key Features

- **Customer & Application Intake**: Record and manage incoming customer profiles, document types, application numbers, tehsils, and referrals.
- **Workflow & Approval Lifecycle**:
  - Track records in **Pending** or **Approved** states.
  - Review pending applications with confirmation dialogs and timestamped approval dates.
- **Financial & Fee Management**:
  - Track **Government Fees** against **Fees Charged to Customers**.
  - Monitor daily revenue versus government liabilities.
- **30-Day Revenue Analytics**:
  - Automatically calculates total revenue and government fees collected over the preceding 30 days.
- **Auditing & Historical Records**:
  - Filter and inspect historical submissions outside the current working date.
- **Modern Admin Panel**:
  - Styled with [Jazzmin](https://django-jazzmin.readthedocs.io/) for a clean, responsive Django administration UI.
- **Role-Based Authentication**:
  - Operator and admin login protection on application routes.

---

## 🛠️ Tech Stack

- **Framework**: Python 3.10+ / 3.11+ & [Django 5.0+](https://www.djangoproject.com/)
- **UI & Dashboard**: Django Templates, Bootstrap 5 / Jazzmin Admin Theme
- **Database**: SQLite (default, easily portable to PostgreSQL or MySQL)
- **Containerization**: Dockerfile included for quick containerized deployment

---

## 📂 Project Architecture

```text
RecordKeeper/
├── c4u/                        # Django project configuration
│   ├── settings.py             # Settings, Jazzmin UI config, and database settings
│   ├── urls.py                 # Core routing (Admin, Services, Auth)
│   └── wsgi.py
├── services/                   # Main services & customer records app
│   ├── models.py               # Customer, Fee, and status models
│   ├── views.py                # Dashboard, revenue, approval, and record views
│   ├── admin.py                # Jazzmin admin integration
│   ├── urls.py                 # Service URL routes
│   └── migrations/             # Database schema migrations
├── templates/                  # Frontend HTML templates
│   ├── index.html              # Daily intake records
│   ├── pending.html            # Pending queue
│   ├── approved.html           # Approved queue
│   ├── past_records.html       # Archive & historical records
│   ├── past_30_days_revenue.html # 30-day revenue analytics
│   └── login.html              # Authentication portal
├── static/                     # Brand logos, icons, and background styles
├── .env.example                # Sample environment configuration
├── .gitignore                  # Git ignore rules for Django and venvs
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container definition
├── manage.py                   # Django management script
└── README.md
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites

- Python 3.10 or higher
- Git
- pip

### 2. Clone the Repository

```bash
git clone https://github.com/Kaditya67/RecordKeeper.git
cd RecordKeeper
```

### 3. Setup Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin & Operator Access)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

---

## 🐳 Running with Docker

You can also run the application inside Docker:

```bash
# Build Docker image
docker build -t recordkeeper .

# Run container
docker run -p 8000:8000 recordkeeper
```

---

## 📜 License

Created for operational and record management demonstration. Feel free to adapt for your own service workflows.

