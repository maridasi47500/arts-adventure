from flask import Flask, render_template, request, session, redirect, url_for
from yourappdb import query_db, get_db
from flask import g
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'any random string'

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()
def set_password(self, password):
    return generate_password_hash(password)

def check_password(self, password_hash, password):
    return check_password_hash(password_hash, password)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from user')
    the_username = "anonyme"
    one_user = query_db('select * from user where username = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (email,username,date_joined,name,country_id,phone,dateofbirth) values (:email,:username,:date_joined,:name,:country_id,:phone,:dateofbirth)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_profile_image", methods=["GET","POST"])
def add_one_profile_image():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into profile_image (user_id,pic) values (:user_id,:pic)",request.form)
        user = query_db('select * from profile_image')
        return render_template("profile_imageform.html", profile_images=user, one_user=one_user, the_title="add new profile_image")
    user = query_db('select * from profile_image')
    one_user = query_db("select * from profile_image limit 1", one=True)
    return render_template("profile_imageform.html", profile_images=user, one_user=one_user, the_title="add new profile_image")

@app.route("/add_one_people_photos", methods=["GET","POST"])
def add_one_people_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into people_photos (profile_image_id,personsname) values (:profile_image_id,:personsname)",request.form)
        user = query_db('select * from people_photos')
        return render_template("people_photosform.html", people_photoss=user, one_user=one_user, the_title="add new people_photos")
    user = query_db('select * from people_photos')
    one_user = query_db("select * from people_photos limit 1", one=True)
    return render_template("people_photosform.html", people_photoss=user, one_user=one_user, the_title="add new people_photos")

@app.route("/add_one_user_video", methods=["GET","POST"])
def add_one_user_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user_video (user_id,vid) values (:user_id,:vid)",request.form)
        user = query_db('select * from user_video')
        return render_template("user_videoform.html", user_videos=user, one_user=one_user, the_title="add new user_video")
    user = query_db('select * from user_video')
    one_user = query_db("select * from user_video limit 1", one=True)
    return render_template("user_videoform.html", user_videos=user, one_user=one_user, the_title="add new user_video")

@app.route("/add_one_radio_voice", methods=["GET","POST"])
def add_one_radio_voice():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into radio_voice (user_id,recording) values (:user_id,:recording)",request.form)
        user = query_db('select * from radio_voice')
        return render_template("radio_voiceform.html", radio_voices=user, one_user=one_user, the_title="add new radio_voice")
    user = query_db('select * from radio_voice')
    one_user = query_db("select * from radio_voice limit 1", one=True)
    return render_template("radio_voiceform.html", radio_voices=user, one_user=one_user, the_title="add new radio_voice")

@app.route("/add_one_subscriber", methods=["GET","POST"])
def add_one_subscriber():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into subscriber (user_id,subscriber_id) values (:user_id,:subscriber_id)",request.form)
        user = query_db('select * from subscriber')
        return render_template("subscriberform.html", subscribers=user, one_user=one_user, the_title="add new subscriber")
    user = query_db('select * from subscriber')
    one_user = query_db("select * from subscriber limit 1", one=True)
    return render_template("subscriberform.html", subscribers=user, one_user=one_user, the_title="add new subscriber")

@app.route("/add_one_comment_photo", methods=["GET","POST"])
def add_one_comment_photo():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into comment_photo (profile_image_id,user_id,content) values (:profile_image_id,:user_id,:content)",request.form)
        user = query_db('select * from comment_photo')
        return render_template("comment_photoform.html", comment_photos=user, one_user=one_user, the_title="add new comment_photo")
    user = query_db('select * from comment_photo')
    one_user = query_db("select * from comment_photo limit 1", one=True)
    return render_template("comment_photoform.html", comment_photos=user, one_user=one_user, the_title="add new comment_photo")

@app.route("/add_one_posts", methods=["GET","POST"])
def add_one_posts():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into posts (user_id,content) values (:user_id,:content)",request.form)
        user = query_db('select * from posts')
        return render_template("postsform.html", postss=user, one_user=one_user, the_title="add new posts")
    user = query_db('select * from posts')
    one_user = query_db("select * from posts limit 1", one=True)
    return render_template("postsform.html", postss=user, one_user=one_user, the_title="add new posts")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route('/register', methods=['GET', 'POST'])
def register():
   print("11")
   if request.method == 'POST':
       print("dsg")
       print(request.form)
       if request.form["password"] == request.form["password_confirmation"]:
           x=query_db("insert into user (email, username, password, country_id, phone, dateofbirth) values (:email, :username, :password, :country_id, :phone, :dateofbirth)", request.form)
           print(x)
           y=query_db("select * from user where username = ? and password = ?", [request.form['username'],request.form['password']])
           print(y)
       session['username'] = request.form['username']
       print("bug")
       return redirect("/?loggedin=true")

   return '''

   <form action="/register" method="post">
      <p><label for="">email</label><input type=email name="email"/></p>
      <p><label for="">name</label><input type = text name = "username"/></p>
      <p><label for="">password</label><input type = password name = "password"/></p>
      <p><label for="">password confirmation</label><input type = password name = "password_confirmation"/></p>
      <p><label for="">country</label><input type = text name = "country_id"/></p>
      <p><label for="">phone</label><input type =telephone name = "phone"/></p>
      <p><label for="">date of birth</label><input type=date name = "dateofbirth"/></p>
      <p><input type="submit" value="Register"/></p>
   </form>
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
   print("11")

   if request.method == 'POST':
       x=query_db("select * from user where username = ? and password = ?", [request.form['username'],request.form['password']])
       print(x)


       print("dsg")
       print(request.form)
       session['username'] = request.form['username']
       print("bug")
       if length(x) > 0:
           return redirect("/?loggedin=true")

   return '''

   <form action="/login" method="post">
      <p><label for="">name</label><input type = text name = "username"/></p>
      <p><input type = password name = "password"/></p>
      <p><input type="submit" value="Login"/></p>
   </form>
'''
