from application import application, db
from util.utils import *

from flask import request, json
from article.models import Article
from sqlalchemy.orm import class_mapper
from flask_cors import cross_origin

def model_to_dict(obj):
    return dict((col.name, getattr(obj, col.name))
                for col in class_mapper(obj.__class__).mapped_table.c)


# 1.1 Create Article List
@application.route('/create_article', methods=['GET', 'POST'])
def createArticle():
    title = request.form.get('title')
    print("----------------")
    print(title)
    if title:
        article_content = request.form.get('article_content')
        print("----------------")
        print(title)
        if article_content:
            author = request.form.get('author')
            print("----------------")
            print(title)
            if author:
                article = Article(title, article_content, author)
                db.session.add(article)
                db.session.commit()
                return json.dumps({"message":"success"}, default=date_handler)
            else:
                return json.dumps({"error":"Author is missing."}, default=date_handler)
        else:
            return json.dumps({"error":"Article content is missing."}, default=date_handler)
    else:
        return json.dumps({"error":"Article title is missing."}, default=date_handler)

# 1.2 Up vote Article
@application.route('/up_vote_article', methods=['GET', 'POST'])
def upVoteArticle():
    article_id = request.form.get('article_id')
    if article_id:
        queryArticle = Article.query.filter_by(id = article_id).first()
        if queryArticle:
            if queryArticle:
                vote = queryArticle.votes
                if vote is None:
                    vote = 0
                queryArticle.votes = vote + 1
                db.session.commit()
                return json.dumps({"message":"success"}, default=date_handler)
            else:
                return json.dumps({"message":"no articles present."}, default=date_handler)
    else:
        return json.dumps({"error":"Article ID is missing."}, default=date_handler)


# 1.3 Get Article Ordered List
@application.route('/article_ordered_list', methods=['GET'])
def getArticleOrderedList():
    queryArticle = Article.query.order_by(Article.votes.desc()).all()
    if queryArticle:
        articleList = []
        for result in queryArticle:
            articleList.append(model_to_dict(result))
        return json.dumps(articleList, default=date_handler)
    else:
        return json.dumps({"message":"no articles present."}, default=date_handler)
