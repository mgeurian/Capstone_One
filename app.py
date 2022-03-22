from flask import Flask, request, render_template, jsonify, session, flash, url_for, redirect
import requests
import json
from requests import Request, Session

from flask_debugtoolbar import DebugToolbarExtension

from secret import API_KEY

from forms import RegisterForm, LoginForm

from models import db, connect_db, User, User_Currency

from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db_educryption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "educryption"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():

    base_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/'
    api_key = '?CMC_PRO_API_KEY=' + API_KEY
    latest_listings_url = base_api + 'listings/latest' + api_key
    request = requests.get(latest_listings_url)
    results = request.json()
    data = results['data']
    return render_template('index.html', currencies=data)


    # *********** GET SINGLE CURRENCY BY SLUG (usually lowercase currency name) ***********

@app.route('/currency/<slug>')
def search_for_currency(slug):
    print('this is the slug: ' + slug)
    base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?'
    api_key = 'CMC_PRO_API_KEY=' + API_KEY
    individual_currency_id_url = base_api + api_key + '&slug=' + slug

    request = requests.get(individual_currency_id_url)
    results = request.json()
    print(results)

    data = results['data']

    list_keys = list(data.keys())[0]
    string_keys = str(list_keys)
    print('this is data key: ', list(data.keys())[0])
    
    currency_data = results['data'][string_keys]

    print('this is the currency_data: ', currency_data)
    
    return render_template('single_currency.html', currency=currency_data)


#  ********** GET SINGLE CURRENCY BY CMC ID **********

@app.route('/currency/<int:id>')
def get_currency(id):
    strid = str(id)
    base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?'
    api_key = 'CMC_PRO_API_KEY=' + API_KEY
    individual_currency_id_url = base_api + api_key + '&id=' + strid


    request = requests.get(individual_currency_id_url)
    results = request.json()
    
    # print(results)
    data = results['data'][strid]
    print('strid')
    print(data)
    return render_template('single_currency.html', currency=data)




    # ******************************************************************************
    # ******************************************************************************
    # ********************* user routes are listed below ***************************
    # ******************************************************************************
    # ******************************************************************************

#  ********** REGISTER NEW USER **********

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data 
        email = form.email.data   
        first_name = form.first_name.data   
        last_name = form.last_name.data   

        new_user = User.register(username, password, email, first_name, last_name)

        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken. Please pick another username')
            return render_template('register.html', form=form)
        session['username'] = new_user.username
        flash('Welcome! Successfully Created Your Account!', "success")
        return redirect(f'/users/{new_user.username}')

    return render_template('register.html', form=form)


#  ********** LOGIN USER **********

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data 

        user = User.authenticate(username, password)

        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['username'] = user.username
            return redirect(f'/users/{user.username}')

        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)


#  ********** LOGOUT USER **********

@app.route('/logout')
def logout_user():
    session.pop('username')
    flash("Goodbye!", "info")
    return redirect(url_for('home_page'))


#  ********** VIEW USER PROFILE **********

@app.route('/users/<username>')
def show_user(username):

    if "username" not in session:
        flash("Please login first!", "danger")
        return redirect(url_for('home_page'))
        
    user = User.query.get(username)

    # returns a list of the current users currencies    
    user_currency = User_Currency.query.filter_by(username=username).all()

    # convert integer ids => string to use in api call
    currency_ids_list = [str(c.currency_id) for c in user_currency]
    currency_ids_string = ",".join(currency_ids_list)

    # take list of users currencies and get data from CMC
    base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?'
    api_key = 'CMC_PRO_API_KEY=' + API_KEY
    users_currencies = base_api + api_key + '&id=' + currency_ids_string

    request = requests.get(users_currencies)
    results = request.json()
    print(results['data']) 
    user_currency_data = results['data']
    print(user_currency_data)

    return render_template("profile.html", user=user, currencies=user_currency_data)


#  ********** ADD USER CURRENCY **********

@app.route('/api/users/<username>/<int:id>/add', methods=["POST"])
def create_user_currency(username, id):
    new_user_currency = User_Currency(
        username=username,
        currency_id=id)

    db.session.add(new_user_currency)
    db.session.commit()
    flash("Currency added", "info")

    # user_currency = User_Currency.query.filter_by(username=username).all()

    response_json = jsonify(currency=new_user_currency.serialize())
    return (response_json, 201)



# ********** DELETE USER CURRENCY **********

@app.route('/api/users/<username>/<int:id>/delete', methods=["DELETE"])
def delete_currency(username, id):
    # user_currency = User_Currency.query.get_or_404(username, id)
    user_currency = User_Currency.query.filter_by(username=username).filter_by(currency_id=id).first_or_404()

    db.session.delete(user_currency)
    db.session.commit()
    response_json = jsonify(message="user's currency has been deleted")
    return response_json



#  ********** DELETE USER **********

@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    """ remove a user and notes from the database """

    if "username" not in session:
        flash("Please login first", "danger")
        return redirect(url_for('home_page'))

    user = User.query.get(username)
    if user.username == session['username']:
        db.session.delete(user)
        db.session.commit()
        session.pop('username')
        flash("The user and their notes have been deleted!", "danger")
        return redirect(url_for('home_page'))



# #  ********** PATHS - NOT IN SERVICE **********

# #  ********** EDIT USER'S PROFILE **********

# @app.route('/users/<username>')
# def edit_user(username):

#     if "username" not in session:
#         flash("Please login first!", "danger")
#         return redirect(url_for('home_page'))

