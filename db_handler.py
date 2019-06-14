import sqlite3

def insertUser(email, password):
     conn = sqlite3.connect('signup.db')
     cur = conn.cursor()
     if isTaken(email, cur):
         return False
     else:
         cur.execute("INSERT INTO user (email,password) VALUES (?,?)",(email, password) )
         cur.execute("INSERT INTO preferences (user_email) VALUES (?)",(email,) )
         conn.commit()
         # msg = "Record successfully added"
         return True
     conn.close()

# inserts preference variable into desired column of preferences table

def toPref(var, column, user_id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("UPDATE preferences SET "+column+" = ? WHERE id = ?", (var, user_id,))
    # cur.execute("UPDATE preferences SET age = 9 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def prefsInit(id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("""UPDATE preferences SET sex = 0, age=1, city_id=306, city_name=San Francisco,
                   budget=2, active=0, Asian=0, American=1, Breakfast=0, Bubble_Tea=0,
                   Cafe=0, Fast_Food=0, Indian=0, Italian=0, Mediterranean=0, Mexican=1, Pizza=1
                   WHERE id = ?""", (user_id,))
    conn.commit()
    conn.close()


# // / / / / / / / / // /  // / / / / / / / / / / / / / / / / / // // / //
# params: user email
# return: user signup ID
def getID(em):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("SELECT id FROM user WHERE email = ?", (em,))
    moo = cur.fetchall()
    return moo

# params: user id
# return: user email
def getUser(id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("SELECT email FROM user WHERE id = ?", (id,))
    yoo = cur.fetchall()
    return yoo[0][0]

# params: user id
# return: (str[]) cuisine preferences
def getCuis(id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()

    cur.execute("""select 'Asian' from preferences where Asian = 1 AND id = """+id+""" union all
                   select 'American' from preferences where American = 1 AND id = """+id+""" union all
                   select 'Breakfast' from preferences where Breakfast = 1 AND id = """+id+""" union all
                   select 'Bubble_Tea' from preferences where Bubble_Tea = 1 AND id = """+id+""" union all
                   select 'Cafe' from preferences where Cafe = 1 AND id = """ +id+ """ union all
                   select 'Fast_Food' from preferences where Fast_Food = 1 AND id = """+id+""" union all
                   select 'Indian' from preferences where Indian = 1 AND id = """+id+""" union all
                   select 'Italian' from preferences where Italian = 1 AND id = """+id+""" union all
                   select 'Mediterranean' from preferences where Mediterranean = 1 AND id = """+id+""" union all
                   select 'Mexican' from preferences where Mexican = 1 AND id = """+id+""" union all
                   select 'Pizza' from preferences where Pizza = 1 AND id = """ + id)


    boo = cur.fetchall()
    return boo

def getCityID(id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("SELECT city_id FROM preferences WHERE id =" +id)
    joo = cur.fetchall()
    return joo

def getCityName(id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("SELECT city_name FROM preferences WHERE id =" +id)
    xoo = cur.fetchall()
    return xoo

def getBudget(id):
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("SELECT budget FROM preferences WHERE id =" +id)
    too = cur.fetchall()
    return too

# return: (BOOL) T if exists/F if not
def validateLogin(em, passw):

    # //TODO: check if email and password match
    conn = sqlite3.connect('signup.db')
    cur = conn.cursor()
    cur.execute("SELECT id from user WHERE EXISTS (SELECT email, password FROM user WHERE email =? AND password =?)", (em, passw,))
    foo = cur.fetchall()
    return foo

def retrieveUsers():
	conn = sqlite3.connect("signup.db")
	cur = conn.cursor()
	cur.execute("SELECT email, password FROM user")
	users = cur.fetchall()
	conn.close()
	return users

def isTaken(em, cur):
    cur.execute("SELECT * FROM user WHERE email =?", (em,))
    doo = cur.fetchall()
    return doo
