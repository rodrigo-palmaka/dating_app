from flask import Flask, request, render_template, redirect, url_for
from find_restaurant import find_restaurant
app = Flask(__name__)

food = find_restaurant()

@app.route('/')
def display():
    # return "Hello"
    return render_template('city.html')

@app.route('/', methods=['POST'])
def city_form():
    variable = request.form['variable']
    # return variable
    food.get_city_ID(variable)
    return redirect(url_for('cuisine_form'))
    # 10784

    # return cuisine_form()

@app.route('/cuisine')
def display2():
    return render_template('cuisine.html')

@app.route('/cuisine', methods=['POST'])
def cuisine_form():
    var = request.form['cuis']
    food.get_cuisine(var)
    food.get_rest_list(food.city_ID, food.cuisine_ID)
    return redirect(url_for('restaurant_form'))


@app.route('/restaurant')
def display3():
    return render_template('restaurant.html', restr=food.res_list)

@app.route('/restaurant', methods=['POST'])
def restaurant_form():
    v = request.form['rest']
    return redirect(food.get_rest_info(v))



    # return str(res.cuisine_ID)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)
