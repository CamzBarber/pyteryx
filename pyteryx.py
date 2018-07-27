import time
import json
import requests
from requests_ntlm import HttpNtlmAuth


class Pyteryx(object):
	
	def __init__(self, host, user, pwrd):
		self.hostname = host
		self.username = user
		self.password = pwrd
		self.session_id = self.__get_session_id(self.hostname, self.username, self.password)
		self.headers = {
			'Accept-Encoding': 'gzip, deflate',
			'X-Requested-With': 'XMLHttpRequest',
			'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'X-Authorization': self.session_id,
			'Connection': 'keep-alive',
			'cache-control': 'no-cache',
			'Content-Type': 'application/json',
    	}


	def __get_session_id(self, host, user, pwrd):
		headers = {
			'Connection': 'keep-alive',
			'Accept': '*/*',
			'cache-control': 'no-cache',
			'X-Requested-With': 'XMLHttpRequest',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
			'Content-Type': 'application/json',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
		}

		data = {'scheme': 'windows', 'parameters': [{'name': 'updateLastLoginDate', 'value': True}]}

		response = requests.post(host + '/gallery/api/auth/sessions/',
								 auth=HttpNtlmAuth(user, pwrd),
								 headers=headers,
								 data=json.dumps(data))

		session_id = 'SPECIAL ' + response.json()['sessionId']
		return session_id


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

	
	def get_workflow_questions(self, app_id):
		params = (
			('useDefaultCredentials', 'true'),
			('_', str(int(round(time.time() * 1000)))),
		)
		
		response = requests.get(self.hostname + '/gallery/api/apps/' + app_id + '/interface',
								auth=HttpNtlmAuth(self.username, self.password),
								headers=self.headers,
								params=params)

		workflow_questions = {
			'status' : response.status_code,
			'results' : response.json()
		}
		
		return workflow_questions
		
		
	def run_workflow(self, app_id, questions=None):
		data = {
			'appPackage': {
				'id': app_id
			},
			'jobName': '',
			'useDefaultCredentials': True,
			'version': '',
			'questions': questions
		}
		
		response = requests.post(self.hostname + '/gallery/api/apps/jobs/',
								auth=HttpNtlmAuth(self.username, self.password),
								headers=self.headers,
								data=json.dumps(data))
		
		workflow_info = {
			'status' : response.status_code,
			'results' : response.json()
		}
		
		return workflow_info

	
	def get_workflow_status(self, instance_id):
		params = (
        	('_', str(int(round(time.time() * 1000)))),
		)
		
		response = requests.get(self.hostname + '/gallery/api/apps/jobs/' + instance_id + '/',
								auth=HttpNtlmAuth(self.username, self.password),
								headers=self.headers,
								params=params)
		
		workflow_status = {
			'status' : response.status_code,
			'results' : response.json()
		}
		
		return workflow_status


	def __get_workflow_output(self, instance_id):
		params = (
			('_', str(int(round(time.time() * 1000)))),
		)

		response = requests.get(self.hostname + '/gallery/api/apps/jobs/' + instance_id + '/output/',
								auth=HttpNtlmAuth(self.username, self.password),
								headers=self.headers,
								params=params)

		outputs = [x['id'] for x in response.json()]

		return outputs


	def __get_workflow_output_token(self):
		params = (
			('_', str(int(round(time.time() * 1000)))),
		)

		response = requests.get(self.hostname + '/gallery/api/auth/token/',
								auth=HttpNtlmAuth(self.username, self.password),
								headers=self.headers,
								params=params)

		return response.json()['token']


	def __get_workflow_data(self, token, instance_id, output_id):
		params = (
			('format', 'raw'),
			('web_token', token),
		)

		response = requests.get(self.hostname + '/gallery/api/apps/jobs/' + instance_id + '/output/' + output_id + '/',
								auth=HttpNtlmAuth(self.username, self.password),
								headers=self.headers,
								params=params)

		return response.text


	def get_workflow_result(self, instance_id):
		output_ids = self.__get_workflow_output(instance_id)
		workflow_data = []
		if len(output_ids) >= 1:
			output_token = self.__get_workflow_output_token()
			for i in output_ids:
				workflow_data.append(self.__get_workflow_data(output_token, instance_id, i))

		workflow_data = {
			'results' : workflow_data
		}

		return workflow_data # should this return dataframe?


	def run_workflow_get_result(self, app_id, questions=None):
		instance_id = self.run_workflow(app_id, questions)['results']['id']
		status_flag = None
		while status_flag != 'Completed':
			status = self.get_workflow_status(instance_id)['results']
			status_flag = status['status']
			print(status['status'], status['disposition'])
			time.sleep(1)

		return self.get_workflow_result(instance_id)
