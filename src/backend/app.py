"""
    [summary] Main application entry point
"""

from flask import Flask, render_template

from . import create_app

app = create_app()

from  backend.router.EnduserRoutes import *
from backend.router.InventoryRoutes import *


@app.route('/')
def index():    
    return render_template('index.html')


if __name__ == "__main__":
    print("application")
