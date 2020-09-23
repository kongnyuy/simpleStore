# Simple store
Simple web application that manages the inventory of shops, stores and similar structures
The application showcases how stock management can be handled through web infrastructure 
It is lite and very portable. Uses sqlite for storing and structuring data
## Concept
Expose stock management via the web and allow endusers to easily and truthfully change the state
of the stock. This is done automatically to ease the work on employees.

## How to run the application
> The application is built upon the python django framework. It contains predefined data entities.

* The requirements.txt file contains the list of dependencies that should be installed before running the application. 

### Installing the dependencies


### Serving the application
simply type <b> python manage.py runserver </b> on the command line to serve the application. ~~NB~~ You should be in the folder *server/store* before running the above command and must have installed the dependencies first. Also, the this is a development serving means not advisable for production.

### All in one go
<pre lang="shell">
python -venv .env
pip install -r requirements.txt
.env\scripts\activate
cd store
python manage.py runserver
</pre>
> The above works for windows. on linux you can use python3 then replace \ with /. <br>
if creating the virtual environment does not work(first command) then install it using pip first.

If the commands run successfully, then you can open your browser and goto address: <b>[http://localhost:8000](http://localhost:8000)</b>

