import time
from session_id import get_session_id


class Pyteryx(object):
	"""docstring for AlterPyx"""
	def __init__(self, host, user, pwrd):
		self.hostname = host
		self.username = user
		self.password = pwrd
		self.session_id = get_session_id(self.hostname, self.username, self.password)
		self.headers = {
			'Accept-Encoding': 'gzip, deflate',
			'X-Requested-With': 'XMLHttpRequest',
			'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'X-Authorization': self.session_id,
			'Connection': 'keep-alive',
			'cache-control': 'no-cache',
    		}

	def get_all_workflows(workspace):
		# gets all workflows from private/collection/district
		millis = int(round(time.time() * 1000))

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
