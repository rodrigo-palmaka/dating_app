# dating_app

Simple Python/Flask app to solve the age old problem, where to take someone on a date!

Simply sign up, select your preferences for going out and choose a date.

The app then returns events and restaurants happing around you in that time frame.

-- - - - - - - - - - -- - - - - -- - - - - - - - - - - - - - -- - - - - - - - - - -

This is my first full-stack project, it was an opportunity to create a backend (Python, Flask, SQLite3) that interacts with multiple external APIs (Zomato, Eventful), familiarize myself with building a 
friendly, aestheitc UI (HTML/CSS) and incorporate very basic (JS/YUI3) scripts for web functionality. The app is currently hosted using (Heroku).

*Note: development is still in progress with features, functionality added constantly. 

*Current version is v1.0

# Run Anywhere!

https://digo-dating-flask.herokuapp.com

## Run Locally

1. Run "py app.py" from directory in terminal.
2. open browser.
3. enter "localhost:5000" into url.

__main_dating_flask.py__: 
  the application itself. Combines helper files into application flow.

__find_events.py__:
  wrapper file used to abstract querying Eventful local events API.
  
__find_restaurant.py__:
  wrapper file used to abstract querying Zomato restaurants API.

__signup.db__:
  database holding all user input information.

__db_handler.py__:
  file used by main app to abstract Database manipulation operations.
