from application import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    article = db.Column(db.String(800))
    author = db.Column(db.String(128))
    votes =  db.Column(db.Integer)

    def __init__(self, title, article, author, vote=0):
            self.title = title
            self.article = article
            self.author = author
            self.votes = vote

    def __repr__(self):
        return '<User {}>'.format(self.title)
