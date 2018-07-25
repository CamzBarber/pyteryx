import time
import json
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

	def get_all_private_workflows(search=None, limit=None, offset=None, package_type=None):
		# gets all workflows from private/collection/district
		params = (
			('search', search),
			('limit', limit),
			('offset', offset),
			('packageType', package_type),
			('_', str(int(round(time.time() * 1000)))),
		)
		
		response = requests.get(self.hostname + '/gallery/api/apps/studio/',
					auth=HttpNtlmAuth(self.user, self.pwrd),
					headers=headers,
					params=params)
		
		private_workflows = {
			'status' : response.status_code,
			'response' : response.json()
		}
		
		return private_workflows

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
