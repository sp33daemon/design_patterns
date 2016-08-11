import time

class Resource:

	def produce(self):
		print("Resource working hard!")
	def available(self):
		print("Resource is available to serve")

class Proxy:

	def __init__(self):
		self.resource = None
		self.occupied = False

	def produce(self):

		print("System is checking if Resource is available ...")

		if self.occupied == False:
			time.sleep(2)
			self.resource = Resource()
			self.resource.available()
		else:
			time.sleep(2)
			print("Resource is busy")

p = Proxy()
p.produce()

p.occupied = True
p.produce()