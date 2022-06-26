# loan

# How to use 

step1:install python 

step2:make virtual environments  
    
    virtaulenv venv

step3: install requirment.txt in loan folder
    
    pip install requirment.txt

step4: Default config makes use of sqlite3 as database:

To get it up and running, run from the loan directory:

    python manage.py migrate
    python manage.py runserver
    
step5: make superuser for admin: 
    
    python manage.py createsuperuser
    
step6: runserver and use:

    python manage.py runserver
    
