from flask import Flask, request, render_template, jsonify, session, flash, url_for, redirect
import requests
import json
from requests import Request, Session
from flask_debugtoolbar import DebugToolbarExtension
from secret import API_KEY
from forms import RegisterForm, LoginForm
from models import db, connect_db, User, User_Currency
from sqlalchemy.exc import IntegrityError
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db_educryption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretkey')
app.config['API_KEY'] = os.environ.get('API_KEY', API_KEY)
print('*****************')
print('*****************')
print('*****************')
print(app.config['API_KEY'])
print(app.config['SECRET_KEY'])
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


def get_by_slug(slug):
    print('this is the slug: ' + slug)
    base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?'
    api_key = 'CMC_PRO_API_KEY=' + API_KEY
    individual_currency_id_url = base_api + api_key + '&slug=' + slug

    request = requests.get(individual_currency_id_url)
    results = request.json()

    data = results['data']

    list_keys = list(data.keys())[0]
    string_keys = str(list_keys)
    
    currency_data = results['data'][string_keys]

    return currency_data

def get_users_currency():
    if "username" not in session:
        currency_ids_list = []
        return currency_ids_list
    else:
        user_currency = User_Currency.query.filter_by(username=session['username']).all()
        currency_ids_list = [c.currency_id for c in user_currency]
        return currency_ids_list


@app.route('/')
def home_page():

    users_currencies = get_users_currency()
        
    """ displays a list of the top 100 currencies """
    base_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/'
    api_key = '?CMC_PRO_API_KEY=' + API_KEY
    latest_listings_url = base_api + 'listings/latest' + api_key
    request = requests.get(latest_listings_url)
    results = request.json()
    data = results['data']
    return render_template('index.html', currencies=data, user_currencies=users_currencies)


    # *********** GET SINGLE CURRENCY BY SLUG (usually lowercase currency name) ***********

@app.route('/currency/<slug>')
def get_currency_view(slug):
    """ display a currency by currency slug """
    currency_data = get_by_slug(slug)
    return render_template('single_currency.html', currency=currency_data)

@app.route('/search')
def search_for_currency():
    """ display a currency by currency slug """
    slug = request.args.get('slug')
    currency_data = get_by_slug(slug)
    return render_template('single_currency.html', currency=currency_data)


#  ********** GET SINGLE CURRENCY BY CMC ID **********

@app.route('/currency/<int:id>')
def get_currency(id):
    
    """ gets user's currencies to compare and render correct add/remove button """

    users_currencies = get_users_currency()

    """ display a currency by coinmarketcap's currency id """
    strid = str(id)
    base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?'
    api_key = 'CMC_PRO_API_KEY=' + API_KEY
    individual_currency_id_url = base_api + api_key + '&id=' + strid

    request = requests.get(individual_currency_id_url)
    results = request.json()
    
    data = results['data'][strid]
    return render_template('single_currency.html', currency=data, user_currencies=users_currencies)

    # ******************************************************************************
    # ******************************************************************************
    # ********************* user routes are listed below ***************************
    # ******************************************************************************
    # ******************************************************************************

#  ********** REGISTER NEW USER **********

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """ register a user and take to profile page """
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
    """ login a user and take to profile page """
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
    """ logout a user and remove session data """
    session.pop('username')
    flash("Goodbye!", "info")
    return redirect(url_for('home_page'))


#  ********** VIEW USER PROFILE **********

@app.route('/users/<username>')
def show_user(username):
    """ display a user's information and their currencies """

    if "username" not in session:
        flash("Please login first!", "danger")
        return redirect(url_for('home_page'))
        
    user = User.query.get(username)

    # returns a list of the current users currencies    
    user_currency = User_Currency.query.filter_by(username=username).all()
    if not user_currency:
        # convert integer ids => string to use in api call
        user_currency_data = 0
    else:
        currency_ids_list = [str(c.currency_id) for c in user_currency]
        currency_ids_string = ",".join(currency_ids_list)
        # take list of users currencies and get data from CMC
        base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?'
        api_key = 'CMC_PRO_API_KEY=' + API_KEY
        users_currencies = base_api + api_key + '&id=' + currency_ids_string
        request = requests.get(users_currencies)
        results = request.json()
        user_currency_data = results['data']
    return render_template("profile.html", user=user, currencies=user_currency_data)


#  ********** ADD USER CURRENCY **********

@app.route('/api/users/<username>/<int:id>/add', methods=["POST"])
def create_user_currency(username, id):
    """ add a currency to user's list of currencies """
    new_user_currency = User_Currency(username=username, currency_id=id)
    db.session.add(new_user_currency)
    db.session.commit()
    response_json = jsonify(currency=new_user_currency.serialize())
    return (response_json, 201)



# ********** DELETE USER CURRENCY **********

@app.route('/api/users/<username>/<int:id>/delete', methods=["DELETE"])
def delete_currency(username, id):
    """ remove a user's currency from the database """
    user_currency = User_Currency.query.filter_by(username=username).filter_by(currency_id=id).first_or_404()
    db.session.delete(user_currency)
    db.session.commit()
    response_json = jsonify(message="currency has been removed")
    return response_json


#  ********** DELETE USER **********

@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    """ remove a user and user's currencies from the database """

    if "username" not in session:
        flash("Please login first", "danger")
        return redirect(url_for('home_page'))

    user = User.query.get(username)
    if user.username == session['username']:
        db.session.delete(user)
        db.session.commit()
        session.pop('username')
        flash("The user and their currencies have been deleted!", "danger")
        return redirect(url_for('home_page'))



# #  ********** PATHS - NOT IN SERVICE **********

# #  ********** EDIT USER'S PROFILE **********

# @app.route('/users/<username>')
# def edit_user(username):

#     if "username" not in session:
#         flash("Please login first!", "danger")
#         return redirect(url_for('home_page'))

