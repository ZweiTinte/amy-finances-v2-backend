# amy-finances-v2-backend

Backend for amy-finances version 2 ! WIP !

Setup a Django Backend:

- pip install pipenv
- pipenv install django
- pipenv install djangorestframework django-cors-headers
- activate env: pipenv shell

Make/Run Migrations:

- python manage.py makemigrations amyFinancesV2Backend
- python manage.py migrate

Run Server on Port 7000:

- python manage.py runserver 7000

Create Admmin User:

- python manage.py createsuperuser
- Admin Route: http://localhost:7000/admin/

Current WIP:

- Setup User Profiles
