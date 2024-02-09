from flask import Flask, render_template

from functions.database import Database

app = Flask(__name__)




@app.route('/')
def hello():
    database = Database('database.db')
    
    #FIXME: database.createTestPost(); 
    posts = database.database.execute('SELECT * FROM posts').fetchall()
    del database

    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def getPost():
    database = Database('database.db')

    post = database.database.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    del database
    return render_template('post.html', post=post)
    