from flask import Flask, render_template, request, redirect, url_for

from functions.database import Database

app = Flask(__name__)
 



@app.route('/')
def index():
    database = Database('database.db')
    database.createTestPost();
    
    posts = database.database.execute('SELECT * FROM posts').fetchall()
    del database

    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def getPost(post_id):
    database = Database('database.db')
    database.createTestPost(); 
    post = database.database.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    del database
    return render_template('post.html', post=post)
    

@app.route('/new', methods=['GET', 'POST'])
def newPost():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        database = Database('database.db')
        database.database.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        database.database.commit()
        del database

        return redirect(url_for('index'))

    return render_template('add_post.html')
