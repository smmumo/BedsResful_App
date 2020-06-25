


from user import User
from werkzeug.security import safe_str_cmp

users = [
   User(1,'bob','asdf')
]


# username_mapping={'bob':{
# 	 'id':1,
# 	 'username':'bob',
# 	 'password':'asdf'

# }}

username_mapping={u.username : u for u in Users}
userid_mapping={u.id : u for u in Users}
# userid_mapping={'1':{
# 	 'id':1,
# 	 'username':'bob',
# 	 'password':'asdf'

# }}

#def aunthenticate(username,password):
	#user=username_mapping.get(username,None)
	#if user and safe_str_cmp(user.password,password):
		#return username_mapping

#def identity(payload):
	#user_id=payload['identity']
	#return userid_mapping.get(user_id,None)

def aunthenticate(username,password):
        user=User.find_by_username(username)
        if user and safe_str_cmp(user.password,password):
            return user

def identity(payload):
    user_id=payload('identity')
    return User.find_by_id(_id)