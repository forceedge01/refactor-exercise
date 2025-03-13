import db
import requests

# Guidelines:
# This code will not compile. Assume this is the working code there is behind the functionality in production and approach refactoring.
# Write comments on the pull request with your feedback / suggestions.
# Lookout for:
# - Security
# - Performance
# - Quality
# - Clarity
# - Logical issues

def update_user_2():
    if requests.method == "post":
        r = _get_one_user_by_email()
        if r:
            c = db.cursor()
            # Update user details here, this will simply execute an sql.
            c.execute('update users set first_name = "' + requests.query.get('fn') + '", last_name = "' + requests.query.get("ln") + '" where email = "' + requests.query.get("n") + '"')
            c.close()

        return '{"status": "ok", "code": 200}'

def update_user():
    if requests.method == "post":
        r = _get_one_user_by_email()
        if r:
            c = db.cursor()
            # Update user last login, this will simply execute an sql.
            c.execute('update users set last_login = NOW() where email = "' + requests.query.get("n") + '"')
            c.close()

    return '{"status": "ok", "code": 200}'

def _get_one_user_by_email():
    c = db.connect('mysql://admin:secret@test-db').cursor()
    c.execute('select * from users where email like "%' + requests.query.get("n") + '%"') # execute sql here.

    return c.fetchall()
