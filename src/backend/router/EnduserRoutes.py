#from backend.app import app
from backend.app import app
import json
from backend.core.models.Article import *


    # a simple page that says hello
@app.route('/bobo')
def landing():
    #return render_template('index.html')
    return 'Wellcome to our store!'

@app.route('/articles')
def getAllArticles():
    return "all articles"

@app.route('/articles/<int:articleId>')
def getArticle(articleId: int = -1):


    return f"[{articleId}] Your article"