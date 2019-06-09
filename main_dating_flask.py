from flask import Flask, request, render_template, redirect, url_for
from find_restaurant import find_restaurant
import sqlite3
import db_handler as handle
from datetime import datetime


app = Flask(__name__)
simpleCuis =  ['Asian', 'American', 'Breakfast', 'Bubble_Tea', 'Cafe',
        'Fast_Food', 'Indian', 'Italian', 'Mediterranean', 'Mexican', 'Pizza']



@app.route("/")
def main():
    return render_template('homepage.html', message='')


@app.route('/', methods = ['POST', 'GET'])
def sign():
   if request.method == 'POST':

      # try:
          ## SIGN-UP
           email = request.form['email1']
           password = request.form['pass1']

           if handle.insertUser(email, password):
          # //TODO: redirect to preferences input page
               id = handle.getID(email)
               # print(id[0][0])
               return redirect(url_for('setPrefs', id=id[0][0]))
           else:
               return main2(signError="Email already used!")

      # except:
           ##LOG-IN
           email = request.form['email2']
           password = request.form['pass2']
           id = handle.getID(email)
           if handle.validateLogin(email, password):
               return redirect(url_for('dash', id=id))
           else:
               return main2(logError="Wrong email or password")

           # //TODO: redirect to welcome pg w calendar
           # return redirect(url_for('cityQuery'))

@app.route('/')
def main2(signError='', logError=''):
    return render_template('homepage.html', message=signError, message2=logError)


@app.route('/signup/<id>')
def prefPage(id):
    return render_template('pref_sign_up.html')

@app.route('/signup/<id>', methods=['POST', 'GET'])
def setPrefs(id):
    find = find_restaurant()


    #City_id
    location = request.form['location']
    if find.get_city_ID(location):
        city_id = find.city_ID
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
            return render_template('pref_sign_up.html', city="Invalid Age Input")
    except:
        return render_template('pref_sign_up.html', city="Invalid Age Input")

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
    # return render_template('dashboard.html', user=handle.getUser(id)[0][0])
    return render_template('calendar.html')

@app.route('/dashboard/<id>', methods=["GET", "POST"])
def dash(id):
    if request.method == "POST":
        selectDate = request.form['selectDate']
        objDate = datetime.strptime(selectDate, '%Y-%m-%d')
        s = datetime.strftime(objDate,'%b %d, %Y')
        # s = objDate.strftime("%B")
        # return suggestPage(id, selectDate)
        # user = handle.getUser(id)
        return redirect(url_for('sugg', id=id, selectDate=s))
        # return render_template('suggest.html', selectDate=s)

#
# # @app.route('/suggestions/<id>')


# @app.route('/dashboard/<id>/<selectDate>')
# def suggestPage(id, selectDate):
#     # user = handle.getUser(id)
#     return render_template('suggest.html', id=id, selectDate=selectDate)

@app.route('/dashboard/<id>/<selectDate>', methods=["GET", "POST"])
def sugg(id, selectDate):
    # a = request.form['test']
    fd = find_restaurant()
    userCuis = handle.getCuis(id) #//TODO: finish db helper to get all cuisines
    cuisIDs = {}
        fd.get_cuisine(i)
    print(id)
    print(userCity)
    return 'done'


    fd.get_rest_list(food.city_ID, food.cuisine_ID)

    return render_template('suggest.html', selectDate=selectDate, sugg=sugg)

    '''



# //TODO: add catch (404) if there is no internet connection


# /////////////////////////////////////////////////////////

@app.route('/user')
def userPage():
    return render_template('welcome.html')
food = find_restaurant()

@app.route('/user', methods=['POST', 'GET'])
def cityQuery():
    if request.method == 'POST':
        cityVar = request.form['cityVar']

        food.get_city_ID(cityVar)

        return redirect(url_for('cuisQuery'))

        # return redirect(url_for('cuisQuery'))

@app.route('/user/cuis')
def wel2():
    return render_template('welcome2.html', city=food.cityName)

#
@app.route('/user/cuis', methods=['POST', 'GET'])
def cuisQuery():
    cuisVar = request.form['cuisVar']

#
    food.get_cuisine(cuisVar)
    food.get_rest_list(food.city_ID, food.cuisine_ID)
    return food.res_list[0]
# return redirect(url_for('cuisine_form'))


    # cuisVar = request.form['cuisVar']
    #
    # food.get_cuisine(cuisVar)
    # food.get_rest_list(food.city_ID, food.cuisine_ID)
    # return food.res_list

## TODO: add in restaurant API functionality



if __name__=='__main__':
    app.run(debug=True)
