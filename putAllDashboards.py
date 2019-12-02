"""
Create or update dashboards stored on disk to selected tenant/environment.

CAUTIONS:

Use PATH_PREFIX to reference the SOURCE path to files
The file is assumed to be the id 
"""

import requests, ssl, os, sys, json, glob

#TARGET: My Personal Managed Environment
# DOESNT WORK DUE TO INSECURE CERT ISSUE
ENV = 'https://******.managed-dev.dynalabs.io/e/*************************************'
TOKEN = '**********'

#TARGET: My Personal SaaS Tenant
ENV = 'https://********.live.dynatrace.com'
TOKEN = '**********'

#SOURCE: Dashboard Templates Local Directory
PATH_PREFIX='dashboardTemplates'

HEADERS = {'Authorization': 'Api-Token ' + TOKEN, 'Content-Type': 'application/json; charset=utf-8'}

PATH = os.getcwd()

def put(list_type, id, payload):
        #print('method: put: ' + list_type + ', ' + id + ', ' + payload)
        print('method: put: ' + list_type + ', ' + id)
        try:
                DIRECTORY_PATH=PATH_PREFIX + '/api/config/v1/' + list_type + '/'
                r = requests.put(ENV + '/api/config/v1/' + list_type + '/' +id, payload, headers=HEADERS)
                print("%s put list: %d" % (list_type, r.status_code))
                #res = r.json()
                #print(res)
        except ssl.SSLError:
                print("SSL Error")

def putFiles(list_type):
        print('method: putFiles: ' + list_type)
        path=PATH_PREFIX + '/api/config/v1/' + list_type + '/*'
        for filename in glob.glob(path):
            with open(filename, 'r') as f:
                put(list_type, os.path.basename(f.name), f.read())

def main():
        print('method: main')
        putFiles('dashboards')

if __name__ == '__main__':
	main()
