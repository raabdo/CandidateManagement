# 
# 🚀 Zfusion Candidate Management System

A simple recruitment portal built with **Django 5.0** and **Bootstrap 5**. This system allows HR teams to manage candidate data, track resumes, and schedule interviews through an interactive calendar.

## ✨ Key Features
* **Candidate Database:** Full CRUD (Create, Read, Update, Delete) for applicant profiles.
* **Resume Management:** Secure file handling for CV uploads.
* **Interactive Schedule:** Custom HTML Calendar view for tracking upcoming interviews.
* **Role-Based Access:** Protected views requiring staff authentication.
* **Modern UI:** Responsive design using the latest Bootstrap 5 components and "Inter" typography.

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/raabdo/CandidateManagement.git
   cd CandidateManagement
   
2. **Setup Virtual environment**
    ```bash
   python -m venv venv
   # Windows
    venv\Scripts\activate
   # Mac/Linux
    source venv/bin/act ivate
   
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
   
4. **Migrations**
    ```bash
   python manage.py migrate
5. **Create Superuser**
    ```bash
   python manage.py createsuperuser
6. **Run the Server
    ```bash
   python manage.py runserver