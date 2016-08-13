class Spanish:
	def __init__(self):
		self.name="Spanish"
	def speak_spanish(self):
		return 'Hola!'

class British:
	def __init__(self):
		self.name="British"
	def speak_english(self):
		return 'Hello!'

class Adapter:

	def __init__(self,object, **adapted_method):
		self._object = object
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		return getattr(self._object, attr)

objects = []

spanish = Spanish()
british = British()

objects.append(Adapter(spanish, speak=spanish.speak_spanish))
objects.append(Adapter(british, speak=british.speak_english))

for item in objects:
	print("{} says {} \n".format(item.name, item.speak()))