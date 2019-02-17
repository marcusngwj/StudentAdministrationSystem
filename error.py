class CustomError(Exception):
	def __init__(self, code, message):
		self.message = message
		self.code = code

	def toString(self):
		return 'Code ' + self.code + ' - ' + self.message