from functools import wraps

def add_html_tag(function):
	"""add html tag"""
	@wraps(function)
	def decorator():
		"""Decorator method"""
		val = function()
		return "<h1>{}</h1>".format(val)
	return decorator


@add_html_tag
def hello_world():
	"""return helloworld"""
	return "Hello, World!"


print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)