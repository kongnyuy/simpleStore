from backend.app import app
import json
#from backend.core.models.Article import *
from backend.core.models.Category import *
from backend.core.persistence.db import Database


# a simple page that says hello
@app.route('/inventory')
def dashboard():
    #return render_template('index.html')
    return 'Wellcome to our inventory!'

@app.route('/category')
def get_article():
    c = Category("Studies", "Items used while studying e.g pen")
    Database.connect()
    c.save();
    return json.dumps(c.__dict__)
