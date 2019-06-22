# dating_app

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
