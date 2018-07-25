import time
import json
import requests
from requests_ntlm import HttpNtlmAuth
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

	def get_all_private_workflows(self, search=None, limit=None, offset=None, package_type=None):
		params = (
			('search', search),
			('limit', limit),
			('offset', offset),
			('packageType', package_type),
			('_', str(int(round(time.time() * 1000)))),
		)
		
		response = requests.get(self.hostname + '/gallery/api/apps/studio/',
					auth=HttpNtlmAuth(self.username, self.password),
					headers=self.headers,
					params=params)
		
		private_workflows = {
			'status' : response.status_code,
			'results' : response.json()
		}
		
		return private_workflows

	def get_all_collection_workflows(self, appLimit=None):
		params = (
			('appLimit', '5'),
			('_', str(int(round(time.time() * 1000)))),
		)
		
		response = requests.get(self.hostname + '/gallery/api/collections/',
					auth=HttpNtlmAuth(self.username, self.password),
					headers=self.headers,
					params=params)
		
		collection_workflows = {
			'status' : response.status_code,
			'results' : response.json()
		}
		
		return collection_workflows
	
	def get_workflow_info(self, app_id):
		response = requests.get(self.hostname + '/gallery/api/apps/' + app_id + '/',
					auth=HttpNtlmAuth(self.username, self.password),
					headers=self.headers)
		
		workflow_info = {
			'status' : response.status_code,
			'results' : response.json()
		}
		
		return workflow_info

	def run_workflow(id):
		# run a workflow
		for key, value in kwargs:
			print(key, value)

	def run_workflow_get_result(id):
		# comment
		pass
