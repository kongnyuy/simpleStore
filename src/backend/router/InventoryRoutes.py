from backend.app import app
import json
from backend.core.models.Article import *


# a simple page that says hello
@app.route('/inventory')
def dashboard():
    #return render_template('index.html')
    return 'Wellcome to our inventory!'
