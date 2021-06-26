# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 21:38:04 2021

@author: Hiral
"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .views import main
    app.register_blueprint(main)
    
    return app

#if __name__=='__main__':
#    create_app().run(debug=True)