class Pyteryx(object):
	"""docstring for AlterPyx"""
	def __init__(self, host, user, pwrd):
		self.hostname = host
		self.username = user
		self.password = pwrd
		self.sessionID = get_sessionID(self.hostname, self.username, self.password)

	def get_all_workflows(workspace):
		# gets all workflows from private/collection/district
		pass

	def get_workflow_info(id):
		# get the details of a workflow based on an ID
		pass

	def run_workflow(id, *args=[], **kwargs={}):
		# run a workflow
		for key, value in kwargs:
			print(key, value)

	def run_workflow_get_result(id):
		# comment
		pass
