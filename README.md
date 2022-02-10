# Todo-List-App
My first project with Django and at the same time i used tailwind css

All steps for Windows computers

First of all open your terminal and install virtualenv 
-> pip install virtualenv 

after this installing let's create a virtual environment
-> virtualenv venv 

venv is our virtual environment name, you can change this name ( Ex : virtualenv env )
The next step is to activate the virtual environment
-> venv\scripts\activate

Now we are ready to download django and django-tailwind
-> pip install django
-> pip install django-tailwind

Let's check packages 
-> pip freeze

Django==4.0.2
django-tailwind==3.1.1

If you see these packages let's continue
Make sure you are in the "todo-list-app" directory in the terminal
finally we run this  project

-> cd todo/static_src
-> npm install
-> cd ../..
-> python manage.py migrate
-> python manage.py runserver 

open another terminal page
-> python manage.py tailwind start  