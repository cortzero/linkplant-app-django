A Django application that imitates the Linktree application that gathers all the links of a user.

# Environment variables
DATABASE_NAME = the name of the databse.
DATABASE_USERNAME = the username to enter the database.
DATABASE_PASSWORD = the password of the user to enter the database.
DATABASE_HOST = the host where the database server is running.
DATABASE_PORT = the port of the host where the database is running.

# How to run
1. Create a virtual environment and activate it.
2. Install the dependencies from the `requirement.txt` file.
3. You need to create a superuser to create a profile. Run `python manage.py createsuperuser` to create a superuser and then run the aplication with `python manage.py runserver` and go to `http://localhost:8000/admin` and type in the credentials of the superuser.
4. Once inside the admin dashboard, click on _Profiles_ and create a new profile so that you can create the links that you want.
5. Go to `http://localhost:8000` and create a few links.
