from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

import os

from translate import translate_text

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

## get the environment variables from the server for the DB
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Configure app for debug mode if the enviornment is set for debug
# Run the app in production otherwise
if os.environ.get("DEBUG") == 'True':
    app.debug = True
    app.config["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
else:
    app.debug = False

mongo = PyMongo(app)

# blog data references the collection within mongo db atlas that holds the blog data
threadDB = mongo.db.threads
userDB = mongo.db.users
postDB = mongo.db.posts

# Landing page
@app.route("/", methods=['GET', 'POST'])
def index():
    # user arrived on the index page, check if they have a username cached or if they are a guest user

    sorted_threads = threadDB.find().sort('_id', -1).limit(4)
    
    translated_threads = list(sorted_threads)

    if(session.get('user')):
        user = userDB.find_one({"username": session["user"]})
        for thread in translated_threads:
            thread['subject'] = translate_text(user['language'], thread['subject'])
        return render_template("index.html", user = userDB.find_one({"username": session["user"]}),  threads=translated_threads)
        
    else:
        session["user"] = "guest"
        return render_template("index.html", user = userDB.find_one({"username": session["user"]}),  threads=sorted_threads)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Login function matches the form input with a database entry and adds user to session cookies
    Returns:
        render template login.html
    """
    if request.method == "POST":
        # see if the username entered in the login form is in the database
        userInfo = userDB.find_one({"username": request.form.get("username")})

        # the username is in the database, now check if the password is correct
        if(userInfo != None):
            userName = request.form.get("username")
            # password is correct, go to index page
            if(userInfo["password"] == request.form.get("password")):
                session["user"] = userName
                flash(f'Welcome back {userName}!'
                )
                return redirect(url_for("index"))
            else:
                # password is incorrect, reset login form
                flash("Incorrect password")
                session["user"] = "guest"
                return render_template("login.html", user = userDB.find_one({"username": session["user"]}))
        else:
            # there is no user with this name in the database, reset login form
            flash("No user account with this name exists")
            session["user"] = "guest"
            return render_template("login.html", user = userDB.find_one({"username": session["user"]}))
    return render_template("login.html", user = userDB.find_one({"username": session["user"]}))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """
    Signup function to add users to the database
    Returns:
        render signup.html
    """
    if request.method == 'POST':
        # Check if user and email are already in the database
        user_exists = userDB.find_one({
            'username': request.form.get('username').lower()
        })
        email_exists = userDB.find_one({'email': request.form.get('email')})
        # Flash error messages and return user to signup page
        if user_exists:
            flash('Username already taken')
            return redirect(url_for('signup'))
        elif email_exists:
            flash('Email already in use!')
            return redirect(url_for('signup'))
        # If there are no conflicts get the data from the form and create the user in database
        else:
            register = {
                'username': request.form.get('username'),
                'email': request.form.get('email'),
                'password': request.form.get('password'),
                'avatar': request.form.get('profile_img'),
                'language': request.form.get('language'),
                'isAdmin': False,
            }
            userDB.insert_one(register)
            # Add user to session cookies
            session['user'] = request.form.get('username')
            flash(
                f'Account created {request.form.get("username")}. Welcome aboard!',
            )
            return redirect(url_for('index'))
    return render_template('signup.html', user = userDB.find_one({'username': session['user']}))

@app.route('/get_all_threads')
def get_all_threads():
    """
    Query the database for all threads and sort them by most recent.
    Store sorted results in <sorted_threads> variable to be passed to template render
    Returns:
        render_template threads.html
    """
    user=userDB.find_one({'username': session['user']})
    # Update the number of posts in each thread in the Database
    threads = threadDB.find()
    for thread in threads:
        threadID = str(thread['_id'])
        number_of_posts = postDB.count_documents({'subjectID': threadID})
        thread['posts'] = number_of_posts
        threadDB.replace_one({'_id': ObjectId(threadID)}, thread)

    # Sort threads by most recent first and translate them
    sorted_threads = threadDB.find().sort('_id', -1)
    translated_threads = list(sorted_threads)

    # Pagination
    page = request.args.get('page', type=int) # page number is fed in via url
    POSTS_PER_PAGE = 4

    # find what post is the first post on this particular page
    firstPostToList = page * POSTS_PER_PAGE

    lastPostToList = firstPostToList + POSTS_PER_PAGE

    # translate the thread details only for the threads that will appear on
    # this particular page
    translated_threads = translated_threads[firstPostToList:lastPostToList]

    for thread in translated_threads:
            thread['subject'] = translate_text(user['language'], thread['subject'])
            thread['content'] = translate_text(user['language'], thread['content'])
    return render_template('allthreads.html', user=user, threads=translated_threads, totalThreads=threadDB.count())

@app.route("/thread")
def thread():
    threadID = request.args.get('threadID', None)

    allPostsInThread=postDB.find({'subjectID': threadID})
    user = userDB.find_one({"username": session["user"]})
    
    thread=threadDB.find_one({'_id': ObjectId(threadID)})
    
    thread['subject'] = translate_text(user['language'], thread['subject'])
    thread['content'] = translate_text(user['language'], thread['content'])

    translatedPosts = list(allPostsInThread)

    for t in translatedPosts:
        author = userDB.find_one({'username': t['author']})
        t['avatar'] = author['avatar']
        t['lang'] = author['language']

    for post in translatedPosts:
        post['content'] = translate_text(user['language'], post['content'])

    return render_template("thread.html", user=user, thread=thread , posts=translatedPosts)
    

@app.route("/logout")
def logout():
    session.pop("user")
    session['user'] = "guest"
    return redirect(url_for("index"))

@app.route("/newthread")
def newthread():
    return render_template("newthread.html")

@app.route("/add_thread_to_db", methods=["POST"])
def add_thread_to_db():
    new_thread = request.form.to_dict()
    new_thread['created_on'] = datetime.now()
    threadDB.insert_one(new_thread)
    return redirect(url_for('index'))

@app.route("/newpost")
def newpost():
    threadID = request.args.get('threadID', None)
    return render_template("newpost.html", user=session["user"], thread=threadDB.find_one({'_id': ObjectId(threadID)}))

@app.route("/add_post_to_db", methods=["POST"])
def add_post_to_db():
    new_post = request.form.to_dict()
    new_post['posted_on'] = datetime.now()
    postDB.insert_one(new_post)
    return redirect(url_for('thread', threadID=new_post['subjectID']))

@app.route("/delete_thread_from_db")
def delete_thread_from_db():
    threadID=request.args.get("threadID", None)
    threadDB.remove({ "_id": ObjectId(threadID) })
    return redirect(url_for("admin_posts"))

@app.route("/delete_post_from_db")
def delete_post_from_db():
    postID=request.args.get("postID", None)
    postDB.remove({ "_id": ObjectId(postID) })
    return redirect(url_for("admin_posts"))

@app.route("/privacy")
def privacy():
    return render_template("privacy.html", user = userDB.find_one({"username": session["user"]}))

@app.route("/terms")
def terms():
    return render_template("terms.html", user = userDB.find_one({"username": session["user"]}))

@app.errorhandler(404)
def page_not_found(e):
    '''
    When error 404 occurs render template for respective page,
    :param e: the error that occurs
    :return render_template of error_404.html
    '''
    return render_template(
        '404.html', user = userDB.find_one({"username": session["user"]}), error=e), 404

@app.route("/report_thread")
def report_thread():
    """
    Route adds flagged: TRUE to the thread that was reported
    Returns:
       redirect to get_all_threads
    """

    threadID = request.args.get("threadID", None)
    thread = threadDB.find_one({'_id': ObjectId(threadID)})
    thread['flagged'] = 'TRUE'
    threadDB.replace_one({'_id': ObjectId(threadID)}, thread)
    flash(
        f'The thread {thread["subject"]} has been reported to the Admin!'
    )
    return redirect(url_for('get_all_threads'))

@app.route("/remove_thread_flag")
def remove_thread_flag():
    """
    Route for the admin to remove the flag from a thread
    Returns:
        redirect to admin_posts route
    """

    threadID = request.args.get("threadID", None)
    thread = threadDB.find_one({'_id': ObjectId(threadID)})
    thread['flagged'] = 'FALSE'
    threadDB.replace_one({'_id': ObjectId(threadID)}, thread)
    flash(
        f'The thread {thread["subject"]} has been unflagged!'
    )
    return redirect(url_for('admin_posts'))


@app.route("/report_post")
def report_post():
    """
    Route adds flagged: TRUE to the post that was reported
    Returns:
       redirect to get_all_threads
    """

    postID = request.args.get("postID", None)
    post = postDB.find_one({'_id': ObjectId(postID)})
    post['flagged'] = 'TRUE'
    postDB.replace_one({'_id': ObjectId(postID)}, post)
    flash(
        f'The post by {post["author"]} has been reported to the Admin!'
    )
    return redirect(url_for('get_all_threads'))

@app.route("/remove_post_flag")
def remove_post_flag():
    """
    Route for the admin to remove the flag from a post
    Returns:
        redirect to admin_posts route
    """
    postID = request.args.get("postID", None)
    post = postDB.find_one({'_id': ObjectId(postID)})
    post['flagged'] = 'FALSE'
    postDB.replace_one({'_id': ObjectId(postID)}, post)
    flash(
        f'The post by {post["author"]} has been unflagged!'
    )
    return redirect(url_for('admin_posts'))

# View for admins to view all posts in the database
@app.route("/admin_posts")
def admin_posts():
    """
    Checks if logged used is admin and queries the database
    for all the flagged threads and posts then returns them to the view
    Returns:
        render template admin_posts.html
    """
    user = userDB.find_one({'username': session['user']})
    if user['isAdmin']:
        flagged_threads = threadDB.find({'flagged': 'TRUE'})
        flagged_posts = postDB.find({'flagged': 'TRUE'})
        return render_template("admin_posts.html", threads=flagged_threads, posts=flagged_posts, user=user)
    else:
        flash('You are not authorized to access this feature')
        return redirect('get_all_threads')

# Set debug status based on enviornment variable
if __name__ == '__main__':
    if app.debug:
        app.run(debug=True)
    else:
        app.run(debug=False)
