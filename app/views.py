from app import (app,
                 db)
from app.models import (User,
                        Movie)
from app.forms import (UserForm,
                       LoginForm, MovieForm)
from flask import (render_template, redirect,
                   request, url_for, flash)
from flask_login  import login_user, logout_user, login_required, current_user
import pygal
#views
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == "POST":
        print("Data not valid")
        if form.validate_on_submit():
            print("Data is valid")
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email = email).first()
            if user is None and not user.check_password(form.password.data):
                flash("Invalid username or password")
            login_user(user)
            return redirect(url_for('movies'))
    return render_template("login.html", form = form)

@app.route("/register", methods =['GET', 'POST'])
def register():
    form  = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(username = form.username.data, email = form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template("register.html", form = form)

    return render_template("register.html", form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


"""
Admin part routes
"""

@app.route('/users/movies', methods = ['GET', 'POST'])
@login_required
def movies():
    form = MovieForm()
    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            movie = Movie(title)
            if movie.get()['Response'] != False:
                print(movie.get())
                rating = float(movie.get_rating())
                print(rating)
                remaing = (100 - rating)
                pie = pygal.Pie()
                pie.title = "Movie Ratings(Showing its success)"
                pie.add("Success", [rating])
                pie.add("failure", [remaing])
                chart = pie.render_data_uri()
                return render_template('result.html', movie = movie, pie = chart, rating = rating)
    return render_template("movie.html", form = form)















