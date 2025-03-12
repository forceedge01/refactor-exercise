from routing import match
from user_updates import update_user_login

match('/', "post", update_user_login())
