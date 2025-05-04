# Clinic EMR

A desktop Electronic Medical Record (EMR) app built with Python and SQLite, designed for managing a small clinic setting.

## Features
- Add/view patient records
- Record patient visits
- Search patient by HN
- Secure login system (upcoming)
- Clean separation of logic using MVC

## Project structure (MVC)
```bash
clinic_EMR/
├── app.py # Main application
├── db.py # DB connection helper
├── login.py # Application main page
├── setup_db.py # Database setup
├── models/ # Database models (SQL logic)
│ └── patient_model.py
│ └── visit_model.py
├── controllers/ # Business logic (glue layer)
│ └── patient_controller.py
│ └── visit_controller.py
├── views/ # GUI (Tkinter Frames)
│ └── add_patient_frame.py
│ └── create_visit_frame.py
│ └── doctor_dashboard_frame.py
│ └── view_patient_frame.py
├── README.md
├── .gitignore
```

## Technologies
- Python 3.x
- Tkinter (GUI)
- SQLite3 (database)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/bhumpat/clinic_EMR
   cd clinic_EMR
   ```

2. **Set up the database**
   ```bash
   python setup_db.py
   ```

3. **Create a new doctor account**
   ```bash
   python users_manage.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## Status
recent MVC update

## Future plan
- Improve UX/UI with modern Tkinter styling
- Password hashing with bcrypt for login secure
- Appointment management feature
- Switch from SQLite to PostgreSQL for scalbiliity
