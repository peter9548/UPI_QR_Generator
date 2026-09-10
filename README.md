# UPI QR Code Generator

A simple Django-based web application that generates a UPI payment QR code from user-provided payment details.

## 🚀 Features

- Generate UPI payment QR codes
- Enter UPI ID
- Enter receiver name
- Enter payment amount
- Add payment note
- Save payment details in the database
- QR code can be scanned using a UPI payment app
- Django Admin panel for managing payment records

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- QRCode Python Library

## 📂 Project Structure

```text
UPI_QR_Generator/
│
├── payment/
│   ├── migrations/
│   ├── templates/
│   │   └── payment/
│   │       └── payment_form.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── manage.py
├── requirements.txt
└── README.md





                                             ⚙️ Installation  Process

Follow the steps below to run this project locally ---
Note - Run all commands in cmd or terminal

1) Clone the Repository -
git clone https://github.com/peter9548/UPI_QR_Generator.git

2) Navigate to the Project Directory-
cd UPI_QR_Generator

3) Create a Virtual Environment-
python -m venv venv

4) Activate the Virtual Environment-
venv\Scripts\activate

5) Install Dependencies-
pip install -r requirements.txt

6) Apply Database Migrations-
python manage.py makemigrations
python manage.py migrate

7) Create a Superuser-
python manage.py createsuperuser
# Enter:
Username
Email
Password

8) Start the Development Server-
python manage.py runserver

9) Open the Application-
# Open your browser and visit:-
http://127.0.0.1:8000/payment/
http://127.0.0.1:8000/admin/
