import json
import requests
from requests_ntlm import HttpNtlmAuth

def get_session_id(host, user, pwrd):
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
