from flask import Flask, request, render_template, redirect, url_for, session
from find_restaurant import find_restaurant
import sqlite3
import db_handler as handle
import find_events as ev
from datetime import datetime
import os
from flask_session import Session

#calendar widget: https://yuilibrary.com/yui/docs/calendar/calendar-simple.html
app = Flask(__name__)


rand = os.urandom(102)

app.config['SECRET_KEY'] = rand
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_object(__name__)
Session(app)




simpleCuis =  ['Asian', 'American', 'Breakfast', 'Bubble_Tea', 'Cafe',
        'Fast_Food', 'Indian', 'Italian', 'Mediterranean', 'Mexican', 'Pizza']
@app.route("/")
def main():
    return render_template('signup.html', message='')


@app.route('/', methods = ['POST', 'GET'])
# SIGN-UP
def sign():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        if not email:
            return signErr(signError="Invalid Email!")
        if not password:
           return signErr(signError="Invalid Password!")
        # returns false if email taken
        insert = handle.insertUser(email, password)
        if insert:
           raw_id = handle.getID(email)
           id = raw_id[0][0]
           handle.prefsInit(id)
           return redirect(url_for('setPrefs', id=id))
        elif not insert:
           return signErr(signError="Email already used!")

@app.route('/')
def signErr(signError=''):
    return render_template('signup.html', message=signError)

@app.route('/login')
def logPage():
    return render_template('login.html', message='')


@app.route('/login', methods=['POST', 'GET'])
def log():
    if request.method == 'POST':
        ##LOG-IN
        email = request.form['email']
        password = request.form['pass']


        if handle.validateLogin(email, password):
            raw_id = handle.getID(email)
            id = raw_id[0][0]
            return redirect(url_for('dash', id=id))
        else:
            return logErr(logError="Incorrect email or password!")

@app.route('/login')
def logErr(logError=''):
    return render_template('login.html', message=logError)



@app.route('/signup/<id>')
def prefPage(id):
    return render_template('pref_sign_up.html')

@app.route('/signup/<id>', methods=['POST', 'GET'])
def setPrefs(id):
    find = find_restaurant()

    location = request.form['location']
    if find.get_city_ID(location):
        city_id = find.city_ID
        handle.toPref(location, "city_name", id)
        handle.toPref(city_id, "city_id", id)
        # print(city_id)
    else:
        return render_template('pref_sign_up.html', city="Invalid City Input")
    #Age
    age = request.form['age']
    try:
        age = int(age)
        if age > 0:
            handle.toPref(age, "age", id)

        else:
            return render_template('pref_sign_up.html', age="Invalid Age Input")
    except:
        return render_template('pref_sign_up.html',  age="Invalid Age Input")

    # Sex
    sex = request.form['sex']
    handle.toPref(sex, "sex", id)

    # for i in request.form["cuis"]:
    # Cuisines
    cuisines = request.form.getlist("cuis")
    if not cuisines:
        cuisines = simpleCuis
    for n in simpleCuis:
        if n in cuisines:
            handle.toPref(1, n, id)
        else:
            handle.toPref(0, n, id)

    # Active
    active = request.form["active"]
    handle.toPref(active, "active", id)

    # Budget
    budget = request.form["budget"]
    handle.toPref(budget, "budget", id)

    return redirect(url_for('dash', id=id))


@app.route('/dashboard/<id>')
def dashPage(id):

    if session.get('restaurants'):
        tempEvents = session['events']
        tempRest = session['restaurants']
        session['events'] = None
        session['restaurants'] = None
        # session.clear()
        return render_template('suggest.html', selectDate=session.get('date'), sugg= tempEvents, rests= tempRest)
    # return render_template('dashboard.html', user=handle.getUser(id)[0][0])
    else:
        return render_template('calendar.html')

@app.route('/dashboard/<id>', methods=["GET", "POST"])
def dash(id):
    if request.method == "POST":
        selectedDate = request.form['selectDate']
        objDate = datetime.strptime(selectedDate, '%Y-%m-%d')
        s = datetime.strftime(objDate,'%b %d, %Y')

        return redirect(url_for('sugg', id=id, selectDate=s))
    else:
        return 'pfffft'



@app.route('/dashboard/<id>/<selectDate>', methods=["GET", "POST"])
def sugg(id, selectDate):
    # a = request.form['test']
    fd = find_restaurant()
    fd.city_ID = handle.getCityID(id)
    rawCuis = handle.getCuis(id)
    cuisIDs = {}
    for i in rawCuis:
        # print(i[0])
        a = i[0].replace("_", " ")
        # TODO: fix output to recognize cuisineID of cuisines w underscore ex.: Bubble_Tea
        cuisIDs[a] = fd.get_cuisine(a)
        cuisList = list(cuisIDs.values())

    # combines all cuisine dicts, lists into one
    listOf3 = []
    dictOf3 = {}
    userBudget = handle.getBudget(id)[0][0]

    while not listOf3:
        for i in cuisList:
            # returns 20 restaurants from each cuisine type
            lis, dic = fd.get_rest_list(fd.city_ID, i)
            num = 1
            # only gets 3 options of each cuis
            for j, t in dic.items():
                if num > 2:
                    break

                if t['price_range'] <= userBudget:
                    listOf3.extend(j)
                    dictOf3.update({j: t})
                    num += 1
        userBudget += 1
    # //TODO: if not enough that match budget, include all (?)
    def pricer(b):
        if b == '1':
            return '$'
        elif b == '2':
            return '$$'
        elif b == '3':
            return '$$$'
        elif b == '4':
            return '$$$$'

    for k, v in dictOf3.items():

        price = pricer(str(v['price_range']))
        v['price_range'] = price
        # bigList.append(k +': '+ v['location']['address'] + " | " + "User Rating: " + str(v['user_rating']['aggregate_rating']) + " | Price: " + price)

    city = handle.getCityName(id)
    liss, dicc = ev.getEvent(city, selectDate)

    session['events'] = dicc
    session['restaurants'] = dictOf3
    session['date'] = selectDate


    # return render_template('suggest.html', selectDate=selectDate, sugg=bigList)
    return redirect(url_for('dash', id=id))



# //TODO (6/20): FIX restaurant <img> size and position.
                # HANDLE case where image is missing, ex. 6/22


# //TODO: add catch [404] if there is no internet connection


# /////////////////////////////////////////////////////////



if __name__=='__main__':
    app.run(debug=True)
