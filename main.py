from routing import match
from user_updates import update_user, update_user_2

match('/', "post", update_user)
match('/update_user_2', "post", update_user_2)
