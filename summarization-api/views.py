# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 21:51:58 2021

@author: Hiral
"""

from flask import Blueprint, jsonify, request


main = Blueprint ('main', __name__)
 
@main.route('/summarize', methods = ['POST'])
def summarize_text():
    from .sumy_placeholder import summarize
    document = request.get_json()
    doc = document["text"]
    summary = summarize(doc)
    json_summary = jsonify({"summary": summary})
    return (json_summary)
    
@main.route('/home')
def home():
    return jsonify({'text': 'Nice', 'id': '1'})
    