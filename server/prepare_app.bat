rem Create a python virtual environment
python -venv .env

rem install project dependencies
pip install -r requirements.txt

rem activate the virtual environment
.env\scripts\activate

rem change directory into the store folder
cd store

rem run the application server
python manage.py runserver