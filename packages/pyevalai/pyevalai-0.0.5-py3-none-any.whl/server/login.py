from server.ldap import ldap_login

def login(username,password):
	"""
	check if (username,password) are valid login credentials. If true: return fullname. Else: return None
	:username: username (string)
	:password: password (string)
	:return: fullname or None
	"""
	user = ldap_login(username, password)
	return None if user is None else user["fullname"]
