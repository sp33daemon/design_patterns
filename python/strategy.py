import types

class Strategy:
	def __init__(self, Instance="Default", function=None):
		self.name = Instance

	def execute(self):
		print("{} is used!".format(self.name))

def strategy_one(self):
	print("{} is used to execute method".format(self.name))

def strategy_two(self):
	print("{} is used to execute method".format(self.name))

s0 = Strategy()
s0.execute()

s1 = Strategy("Strategy one",strategy_one)
s1.execute()

s2 = Strategy("Strategy Two", strategy_two)
s2.execute()