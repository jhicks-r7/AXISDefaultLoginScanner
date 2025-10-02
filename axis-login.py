import requests
from requests.auth import HTTPDigestAuth
import sys

requests.packages.urllib3.disable_warnings()

targets_file = sys.argv[1]
login_endpoints = ['axis-cgi/login.cgi', 'axis-cgi/usergroup.cgi', 'axis-cgi/lightcontrol.cgi']
username = 'root'
password = 'pass'
debug_log_file = 'axis-login-debug.log'

def try_login(target): 
    for endpoint in login_endpoints:
        if target[-1] == '/':
            url = f'{target}{endpoint}'
        else:
            url = f'{target}/{endpoint}'
        
        response=requests.get(f'{target}{endpoint}', auth=HTTPDigestAuth(username, password), verify=False)
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            return False
        elif response.status_code == 404:
            pass
        else:
            with open(debug_log_file, 'a+') as f:
                f.write('-----------\n')
                f.write("Unknown response when authenticating to {}\n".format(URL))
                f.write(response.request.headers)
                f.write('\n')
                f.write(response.text)
                f.write('\n')
            return False
    print("Login URL could not be found for {}".format(target))
    print(response.status_code)
    return False

def load_targets():
    with open(targets_file, 'r') as f:
        targets = f.read().splitlines()
    return targets

def main():
   targets = load_targets()
   for t in targets:
        result = try_login(t)
        if result==True:
            print("{} is using default creds root/pass".format(t))
        if result==False:
            print("{} is NOT using default creds root/pass".format(t))
            
if __name__ == "__main__":
    main()
