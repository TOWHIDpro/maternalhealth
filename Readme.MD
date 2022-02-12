#Open terminal and run all this commands one by one



python -m venv test

test\Scripts\activate

pip install -r requirements.txt

python -m pip install --upgrade pip   #Not mandatory

python manage.py runserver
