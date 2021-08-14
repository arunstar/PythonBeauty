print("Hello Beautyful!")

class Welcome(object):
	"""docstring for Welcome"""
	def __init__(self, arg):
		super(Welcome, self).__init__()
		self.arg = arg

	def say_hello(self):
		print(self.arg)

	@classmethod
	def yes():
		pass

wel = Welcome("Hello")
# print(Welcome.arg)
print(wel.arg)
print()