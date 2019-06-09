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
     # cur.execute("""SELECT cname FROM preferences
     #            CROSS apply ( VALUES ('Asian', Asian),
     #                                ('American', American),
     #                                ('Breakfast', Breakfast),
     #                                ('Bubble_Tea', Bubble_Tea),
     #                                ('Cafe', Cafe),
     #                                ('Fast_Food', Fast_Food),
     #                                ('Indian', Indian),
     #                                ('Italian', Italian),
     #                                ('Mediterranean', Mediterranean),
     #                                ('Mexican', Mexican),
     #                                ('Pizza', Pizza)) ca (cname, data)
     #            WHERE data = 1""")



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

    # cur.execute("""select 'Asian' from preferences where Asian = 1 AND id = 3 union all
    #                select 'American' from preferences where American = 1 AND id = 3 union all
    #                select 'Breakfast' from preferences where Breakfast = 1 AND id = 3 union all
    #                select 'Bubble_Tea' from preferences where Bubble_Tea = 1 AND id = 3""")
    # '''
    # cur.execute("""select        case
    #
    # when American = 1 and id = 3 then 'American'
    # when Breakfast = 1 and id = 3 then 'Breakfast'
    # when Bubble_Tea = 1 and id = 3 then 'Bubble_Tea'
    # when Cafe = 1 and id = 3 then 'Cafe'
    # when Fast_Food = 1 and id = 3 then 'Fast_Food'
    # when Indian = 1 and id = 3 then 'Indian'
    # when Italian = 1 and id = 3 then 'Italian'
    # when Mediterranean = 1 and id = 3 then 'Mediterranean'
    # when Mexican = 1 and id = 3 then 'Mexican'
    # when Pizza = 1 and id = 3 then 'Pizza'
    #
    # end as List
	# from preferences""")
    # '''
    boo = cur.fetchall()
    return boo

def validateLogin(em, passw):
    # returns BOOL: T if exists/F if not
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
