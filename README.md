# Codemonk-TextSearch
This git repository is hosted on Render.com ( https://codemonk-textsearch.onrender.com/ )

    ---------------Steps to Run this Django App(for Windows)---------------

1. Download this git repository.
2. Unzip the repository  where you want to keep this project.
3. Go insite the parent folder "Codemonk-TextSearch-main" using command prompt/any other terminal.
4. Here we have to create a new environment for this django app.
5. Run the command "python -m venv django_env" or "virtualenv django_env" -- Here django_env is the name of environment.
6. Now run "django_env/Scripts/activate" -- This command will activate your django environment.
7. Go to "Codemonk-TextSearch-main > Core>" 
8. Run "pip install -r requirements.txt" -- This will install all the required packages mentioned
     in the requirements.txt file.
9. Run "python manage.py makemigrations" and then  "python manage.py migrate"
9. Now run "python manage.py runserver"



-----------------------Commands for creating a docker image------------------------------

1.Build the image:
    RUN: docker build -t filename . 

2.To run the docker image:
    RUN: docker run -d -p 8080:8000 "Image repository/Image id"




