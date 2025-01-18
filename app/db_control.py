import sqlite3

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS db 
                        (name TEXT PRIMARY KEY, link name)''')
        conn.commit()

def check_exsist(name):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("SELECT name FROM db WHERE name = ?", (name,))
        res = cur.fetchone()
        if res:
            return True
        return False
    
def add_rec(link, name):
    with sqlite3.connect('database.db') as conn:
        conn.execute("INSERT INTO db (link, name) VALUES (?, ?)", (link, name,))
        conn.commit()

def get_rec(name):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("""SELECT link FROM db WHERE name = ?""", (name,))
        return cur.fetchone()

def update_name(name, new_name):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("""UPDATE db SET name = ? WHERE name = ?""", (new_name, name,))
    
def update_link(name, new_link):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("""UPDATE db SET link = ? WHERE name = ?""", (new_link, name,))

def delete_rec(name):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("""DELETE FROM db WHERE name = ?""", (name,))