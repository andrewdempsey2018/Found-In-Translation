from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import os

from translate import translate_text

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# get the environment variables from the server for the DB
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

app.config["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

# Set debug status based on enviornment variable
if os.environ.get("DEBUG") == 'True':
    app.debug = True
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
    if(session.get('user')):
        return render_template("index.html", user = userDB.find_one({"username": session["user"]}),  threads=threadDB.find())
    else:
        session["user"] = "guest"
        return render_template("index.html", user = userDB.find_one({"username": session["user"]}),  threads=threadDB.find())


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
                return render_template("index.html", user = userDB.find_one({"username": session["user"]}), threads=threadDB.find())
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
                'isAdmin': 'false',
            }
            userDB.insert_one(register)
            # Add user to session cookies
            session['user'] = request.form.get('username')
            flash(
                f'Account created {request.form.get("username")}. Welcome aboard!',
            )
            return redirect(url_for('index'))
    return render_template('signup.html', user = userDB.find_one({'username': session['user']}))


@app.route("/thread")
def thread():
    threadID = request.args.get('threadID', None)

    allPostsInThread=postDB.find({'subjectID': threadID})
    
    user = userDB.find_one({"username": session["user"]})
    
    translatedPosts = list(allPostsInThread)

    for post in translatedPosts:
        post['content'] = translate_text(user['language'], post['content'])

    return render_template("thread.html", user=user, thread=threadDB.find_one({'_id': ObjectId(threadID)}), posts=translatedPosts)
    


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
    threadDB.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

@app.route("/newpost")
def newpost():
    threadID = request.args.get('threadID', None)
    return render_template("newpost.html", user=session["user"], thread=threadDB.find_one({'_id': ObjectId(threadID)}))

@app.route("/add_post_to_db", methods=["POST"])
def add_post_to_db():
    postDB.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

@app.route("/delete_thread_from_db")
def delete_thread_from_db():
    threadID=request.args.get("threadID", None)
    threadDB.remove({ "_id": ObjectId(threadID) })
    return redirect(url_for("index"))

@app.route("/delete_post_from_db")
def delete_post_from_db():
    postID=request.args.get("postID", None)
    postDB.remove({ "_id": ObjectId(postID) })
    return redirect(url_for("index"))

# View for admins to view all posts in the database
@app.route("/admin_posts")
def admin_posts():
    return render_template("admin_posts.html", posts=postDB.find())

# Set debug status based on enviornment variable
if __name__ == '__main__':
    if app.debug:
        app.run(debug=True)
    else:
        app.run(debug=False)
