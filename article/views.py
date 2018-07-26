from flask import render_template
from application import application

@application.route('/')
def artical_list():
    return render_template('article/article_list.html')

@application.route('/create_article')
def create_article():
    return render_template('article/create_article.html')
