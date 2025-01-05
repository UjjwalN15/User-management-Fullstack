# User-Management-System-Fullstack
This is a User Management system where I divided users group into two category: one is enterprise user and other is normal user. An enterprise user can create , edit, delete view and like a post and change his/her password whereas a normal user can only view post, like post and change his/her password. This project was created in Django using Django's MVT architecture.
1. Install Prerequisites
  Python: Install Python (version 3.8 or higher recommended) from python.org.
  Virtual Environment (Optional but Recommended): Use venv or virtualenv to create an isolated Python environment.
2. Clone the Project
  git clone <repository_url>
  cd <project_folder>
3. Set Up Virtual Environment
  Create a virtual environment:
    python -m venv venv
  Activate the virtual environment:
    On Windows:
      venv\Scripts\activate
    On Mac/Linux:
      source venv/bin/activate
4. Install Dependencies
  Install the required packages using pip:
  pip install -r requirements.txt
5. Set Up Environment Variables
  Create a .env file in the project directory (if required by the project).
  Add necessary environment variables.
6. Apply Migrations
  Migrate the database schema:
    python manage.py makemigrations
    python manage.py migrate
7. Create a Superuser (Optional)
  The project has an admin interface, create a superuser account:
    python manage.py createsuperuser
8. Run the Development Server
  Start the server:
    python manage.py runserver
  Open the server in a browser:
    By default, the server runs at: http://127.0.0.1:8000
10. Troubleshooting Common Issues
  Missing Modules: If some packages are missing, check the requirements.txt and install them.
  Database Errors: Ensure the database credentials in settings.py are correct and the database is running.
  Static Files Not Loading: Use python manage.py collectstatic to gather static files.

If you have any confusions regarding the project fell free to message me
Facebook : https://www.facebook.com/profile.php?id=100091491353441
WhatsApp : +9779808986000

Thank you.
