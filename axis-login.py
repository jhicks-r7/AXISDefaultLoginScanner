import requests
from requests.auth import HTTPDigestAuth
import sys

target_file = sys.argv[1]
login_endpoints = ['axis-cgi/login.cgi', 'axis-cgi/usergroup.cgi', 'axis-cgi/lightcontrol.cgi']
username = 'root'
password = 'pass'


def try_login(target): 
    for endpoint in login_endpoints:
        response=requests.get(f'{target}/{endpoint}', auth=HTTPDigestAuth(username, password), verify=False)
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            print(response)
            return False
        elif response.status_code == 404:
            print("endpoint {} not found".format(endpoint))
        else:
            print("Unknown status code: {}".format(response.status_code))

    print("Unable to login to {}".format(target))
    return False

def load_targets():
    with open(target_file, 'r') as f:
        targets = f.read().splitlines()
    return targets

def main():
   targets = load_targets()
   for t in targets:
        result = try_login(t)
        if result==True:
            print("{} is using default creds root/pass".format(t))
        if result==False:
            print("{} NOT is using default creds root/pass".format(t))
            
if __name__ == "__main__":
    main()
