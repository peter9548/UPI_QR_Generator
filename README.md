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
