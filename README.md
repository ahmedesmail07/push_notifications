﻿# Notifications

Push Notifications is a simple, fast application built with Django, HTML, CSS, and JavaScript for real-time push notifications. The app is designed to use Django Channels to handle WebSocket connections and asynchronous tasks. It's also deployed on Vercel and Railway.

## Installation

1. Clone the repository:

- [git clone](https://github.com/ahmedesmail07/push_notifications.git)

2. Install the project dependencies:

   - cd push_notifications
   
   - pip install -r requirements.txt

3. Migrate the database:

   - python manage.py migrate

4. Run the development server:

   - python manage.py runserver

you can also run the application from uvicorn:

   - uvicorn django_project.asgi:application --port 8000 --workers 4 --log-level debug --reload

The development server should now be running at `http://localhost:8000/`.

## Usage

Once the development server is running, you can access the Push Notifications app by navigating to `http://localhost:8000/` in your web browser. From there, you can send push notifications to all connected clients by entering a message in the input field and clicking the "Send Notification" button.

## Deployment

To deploy the Push Notifications app to Vercel and Railway, follow these steps:

1. Create an account on Vercel and Railway.

2. Follow the deployment instructions provided by the Vercel and Railway documentation.

- [Deploying Django to Vercel](https://vercel.com/guides/deploying-django-to-vercel)

## Repository Contents

- `django_project`: This directory contains the main settings and configurations for the Django project.
- `notifications`: This directory contains the Django app that handles the WebSocket connections and asynchronous tasks for sending push notifications.
- `staticfiles/admin`: This directory contains the static files for the Django admin interface.
- `db.sqlite3`: This is the default SQLite database used by the project.
- `manage.py`: This is the Django management script for running various commands.
- `README.md`: This file contains information about the Push Notifications app and how to use it.

## Contact

If you have any questions or concerns, please feel free to contact me at [my gmail](mailto:ahmedismail332211@gmail.com).
