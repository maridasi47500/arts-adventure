from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,country_id,phone,email,profile_mode) values (:username,:country_id,:phone,:email,:profile_mode)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (user_id,myphoto) values (:user_id,:myphoto)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

