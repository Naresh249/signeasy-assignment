import jwt

from rest_framework import permissions

from books.constants import SECRET_KEY_CLIENTS

class IsValidUserBookService(permissions.BasePermission):
	"""
	Validating users for book service
	"""
	def has_permission(self, request, view):
		"""
		Checking if user is valid or not
		"""
		if request.user.is_authenticated:
			return True
		else:
			jwt_token = request.META.get('HTTP_AUTHORIZATION')
			# For now this is hardcoded later we can have scret keys based on filter
			secret_key = 'signeasy'
			# Validation JWT token
			try:
				res = jwt.decode(jwt_token, secret_key)
				return True
			except Exception as e:
				return False
	# Object level permission also can be implemented here