from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'DB': 'my_db'
}
db = MongoEngine(app)

class Article(db.Document):
    title = db.StringField(max_length=100)
    content = db.StringField()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        article = Article(title=request.form['title'], content=request.form['content'])
        article.save()
        return redirect(url_for('index'))
    else:
        articles = Article.objects.all()
        return render_template('index.html', articles=articles)

@app.route('/article/<article_id>', methods=['GET', 'PUT', 'DELETE'])
def article(article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'GET':
        return render_template('article.html', article=article)
    elif request.method == 'PUT':
        article.title = request.form['title']
        article.content = request.form['content']
        article.save()
        return redirect(url_for('article', article_id=article_id))
    elif request.method == 'DELETE':
        article.delete()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)