import db
import requests

def update_user_login():
    if requests.is_post():
        c = db.connect('connection string').cursor()
        c.execute('select * from users where email like "%' + requests.query.get("n") + '%"') # execute sql here.
        r = c.fetchall()
        if r:
            # Update user last login, this will simply execute an sql.
            c.execute('update users set last_login = NOW() where email = "' + requests.query.get("n") + '"')
            c.close()

    return '{"status": "ok", "code": 200}'
