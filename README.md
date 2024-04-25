# text2image
First of all open up the project in VS code or any other code editor of your choice 
Then make a virtual environment
Then after activating the virtual environment install the required packages from the requirements.txt file

After installing the required packages, you'll need to set up the database configuration. If you haven't already, create a local.py file in the same directory as your settings.py file, and define your database configuration there.

Once your database configuration is set up, you can proceed to apply any initial migrations to set up your database schema. Use the following command:

python manage.py migrate


This command will create the necessary tables in your database according to the models defined in your Django app.

With the database set up, you can now run the development server:

python manage.py runserver

This command will start the development server, and you can access your application by navigating to the specified URL, usually http://127.0.0.1:8000/, in your web browser.

i have configured the celery configuration in settings.py file
you just have to write the command for sawing the parallel tasks for image generation

celery -A your_project_name worker -l info

