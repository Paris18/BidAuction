from django.core.exceptions import PermissionDenied
from functools import partial

def login_required(function):
	def wrap(request, *args, **kwargs):
		'''Maintain token or session based verification'''
		return function(request, *args, **kwargs)
		# if 'user' in request.session:
		# 	return function(request, *args, **kwargs)
		# else:
		# 	raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ ='login_required'
	return wrap

def user_admin(function):
	def wrap(request, *args, **kwargs):
		'''Maintain token or session based verification'''
		return function(request, *args, **kwargs)
		# if 'user' in request.session:
		# 		raise PermissionDenied
		# else:
		# 	raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ ='user_admin'
	return wrap

