import re
import requests
from bs4 import BeautifulSoup


URL = 'https://www.acmicpc.net'


class Network:

    def __init__(self):
        self.user_id = None
        self.cookie = None

    def login(self, user_id, user_password):
        url = '%s/%s' % (URL, 'signin')
        data = {'login_user_id': user_id, 'login_password': user_password}
        res = requests.post(url=url, data=data, allow_redirects=False)

        if res.status_code != 302:
            return True, str(res.status_code)
        if not 'Set-Cookie' in res.headers:
            return True, 'Cookie not found'
        if not 'Location' in res.headers:
            return True, 'Redirecting error'
        if 'error' in res.headers['Location']:
            return True, 'Login failed for user'
       
        cookie = ''
        flag_cfduid = False
        flag_oj = False
        for element in re.split(',| ', res.headers['Set-Cookie']):
            if '__cfduid' in element:
                cookie += element + ' '
                flag_cfduid = True
            if 'OnlineJudge' in element:
                cookie += element
                flag_oj = True

        if not (flag_cfduid and flag_oj):
            return True, 'Invalid cookie'

        self.user_id = user_id
        self.cookie = cookie
        return False, 'Login succeed'

    def get_problem_list(self):
        if self.user_id is None:
            return True, 'Login is required'

        url = '%s/%s/%s' % (URL, 'user', self.user_id)
        res = requests.get(url=url)

        if res.status_code != 200:
            return True, str(res.status_code)

        soup = BeautifulSoup(res.text, 'html.parser')
        selector = soup.find_all('div', {'class': 'panel-body'})[0].find_all('span', {'class': 'problem_number'})
        if selector is None:
            return True, 'Selector is none'

        problem_list = []
        for problem_id in selector: 
            problem_list.append(problem_id.text)

        return False, problem_list

    def analyze_problem(self, problem_id, language_id='-1'):
        if self.user_id is None:
            return True, 'Login is required'

        url = '%s/%s' % (URL, 'status')
        params = {'problem_id': problem_id, 'user_id': self.user_id, 'language_id': language_id, 'result_id': '4'}
        res = requests.get(url=url, params=params)
            
        if res.status_code != 200:
            return True, str(res.status_code)

        soup = BeautifulSoup(res.text, 'html.parser')
        selector = soup.find(id='status-table').tbody.tr.find_all('td')
        if selector is None:
            return True, 'Selector is none'

        solved_problem = {}
        solved_problem['submission_id'] = selector[0].text
        solved_problem['problem_id'] = selector[2].a.text
        solved_problem['problem_title'] = selector[2].a['title']
        solved_problem['memory'] = selector[4].text
        solved_problem['time'] = selector[5].text
        solved_problem['language'] = selector[6].text
        solved_problem['length'] = selector[7].text
        solved_problem['date'] = selector[8].a['title']
        
        return False, solved_problem

    def download_source(self, submission_id):
        if self.cookie is None:
            return True, 'Login is required'

        url = '%s/%s/%s/%s' % (URL, 'source', 'download', submission_id)
        headers = {'Cookie': self.cookie}
        res = requests.get(url=url, headers=headers)

        if res.status_code != 200:
            return True, str(res.status_code)

        return False, res.text

    def get_user_id(self):
        if self.user_id is None:
            return True, 'Login is required'
        return False, self.user_id
