# RecordKeeper

**RecordKeeper** is a Django-based record-keeping system designed for small shops and operators to efficiently manage customer details, application approvals, government fee payments, and revenue tracking.

---

## Features

<details>
<summary>Click to expand Features</summary>

- **Customer Management:** Track detailed information for customers and applications.  
- **Application Workflow:** Approve or mark applications as pending, with operator and approval tracking.  
- **Government Fee Tracking:** Monitor government-related payments and calculate balances.  
- **Revenue Reporting:** View revenue from the past 30 days with automated reporting.  
- **User Authentication:** Supports login/logout for multiple users and operators.  
- **Approval System:** Process record approvals securely, including confirmation steps.  
- **Historical Records:** Access past customer and application records for audits or re-verification.  
- **Multi-user Support:** Track actions by each user/operator for improved accountability.  

</details>

---

## Setup Instructions

<details>
<summary>Click to expand Setup</summary>

### 1. Clone the Repository
```bash
git clone https://github.com/Kaditya67/RecordKeeper.git
cd RecordKeeper
```

### 2. Install Dependencies
Ensure Python 3.8+ and pip are installed.
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
Visit http://127.0.0.1:8000 in your browser.
</details>

## Usage
<details> <summary>Click to expand Usage Instructions</summary>

Login: Use provided credentials or superuser login.

Add/View Customers: Navigate to customer management via the dashboard.

Approve/Mark Applications: Check application status and perform approval actions.

Report Revenue & Fees: Use revenue and fee calculation views for analytics.

View History: Access previous records for references or audits.

</details>
