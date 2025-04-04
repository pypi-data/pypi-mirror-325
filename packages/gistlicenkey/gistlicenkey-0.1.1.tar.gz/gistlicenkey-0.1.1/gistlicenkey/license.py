#!/usr/bin/env python3
import os
import json
import string
import random
import secrets
import hashlib
import requests

from datetime import datetime, timedelta

class LicenseServer:
    
    server = 'https://api.github.com/gists'
    
    def __init__(self, token: str = None):
        if token is None:
            raise TyperError('missing required positional argument: token')
        
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Windows x86_64; rv:91.0) Gecko/20100402 Firefox/91.0'
        })
    
    def all_file(self):
        files = []
        gists = self.session.get(self.server)
        gists.raise_for_status()
        for response in gists.json():
            files.append({
                'id': response['id'],
                'owner': response['owner']['login'],
                'public': response['public'],
                'filename': response['files'][list(response['files'].keys())[0]]['filename'],
                'description': response['description'],
                'created': response['created_at'],
                'updated': response['updated_at'],
                'raw_url': response['files'][list(response['files'].keys())[0]]['raw_url']
            })
        return files
    
    def file_name(self, id: str):
        response = self.session.get(os.path.join(self.server, id))
        response.raise_for_status()
        response = response.json()
        return list(response['files'].keys())[0]
    
    def create_file(
            self,
            public: bool = False,
            content: any = None,
            filename: str = None,
            description: str = None,
        ):
        
        if content is None: content = []
        if filename is None: filename = str(secrets.token_hex(16))
        if description is None: description = ''
        if isinstance(content, list | dict): content = json.dumps(content, indent=4)
        
        data = {
            'description': description,
            'public': public,
            'files': {
                filename: {
                    'content': content
                }
            }
        }
        
        response = self.session.post(self.server, json=data).json()
        return {
            'id': response['id'],
            'owner': response['owner']['login'],
            'public': response['public'],
            'filename': response['files'][list(response['files'].keys())[0]]['filename'],
            'description': response['description'],
            'created': response['created_at'],
            'updated': response['updated_at'],
            'raw_url': response['files'][list(response['files'].keys())[0]]['raw_url']
        }
    
    def delete_file(self, id: str):
        response = self.session.delete(os.path.join(self.server, id))
        return True if response.status_code == 204 else False
    
    def read_file(self, id: str, filename: str):
        response = self.session.get(os.path.join(self.server, id)).json()
        return json.loads(response['files'][filename]['content'])

    def update_data(self, id: str, data: any, filename: str):
        response = self.session.patch(os.path.join(self.server, id), json=data).json()
        return response['files'][filename]['content']
    
    def delete_data(self, id: str):
        filename = self.file_name(id)
        response = self.session.patch(os.path.join(self.server, id), json={'files': {filename: ''}})
        return True if response.status_code == 200 else False
    
    def create_key(
            self,
            id: str,
            user: str,
            machine: str,
            premium: bool = False,
            expired: int = 0,
            filename: str = None
        ):
        
        key = '-'.join(''.join(random.choices(string.ascii_uppercase, k=4))for _ in range(4))
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        expired = (datetime.now() + timedelta(days=expired)).strftime('%Y-%m-%d %H:%M:%S')
        newdata = {
            'key': key,
            'user': user,
            'premium': premium,
            'created': created,
            'expired': expired,
            'machine': machine,
        }
        if filename is None: filename = self.file_name(id)
        content = self.read_file(id, filename)
        content.append(newdata)
        data = {
            'files': {
                filename: {
                    'content': json.dumps(content, indent=4)
                }
            }
        }
        update = self.update_data(id, data, filename)
        return update
    
    def delete_key(
            self,
            id: str,
            key: str,
            filename: str = None
        ):
        if filename is None: filename = self.file_name(id)
        content = self.read_file(id, filename)
        content = [item for item in content if item['key'] != key]
        data = {
            'files': {
                filename: {
                    'content': json.dumps(content, indent=4)
                }
            }
        }
        update = self.update_data(id, data, filename)
        return update

class LicenseClient:
    
    link = 'https://timeapi.io/api/Time/current/zone?timeZone=Asia/Jakarta'
    path = ['/bin', '/etc', '/lib', '/root', '/sbin', '/usr', '/var']

    def __init__(self, gist: str):
        self.gist = gist
    
    def machine(self):
        machine = []
        for line in self.path:
            try:
                code = os.stat(line).st_ino
                machine.append(str(code))
            except Exception:
                pass
        return hashlib.sha256(''.join(machine).encode()).hexdigest()
    
    def verify_key(self, key: str):
        try:
            response = requests.get(self.gist)
            response.raise_for_status()
            license = response.json()
            machine = self.machine()
            datenow = requests.get(self.link).json()
            for data in license:
                if data['key'] == key and data['machine'] == machine:
                    expired = data['expired']
                    expired = datetime.strptime(expired, '%Y-%m-%d %H:%M:%S')
                    datenow = '{year}-{month}-{day} {hour}:{minute}:{seconds}'.format(**datenow)
                    datenow = datetime.strptime(datenow, '%Y-%m-%d %H:%M:%S')
                    if not datenow >= expired:
                        return {'status': True, 'license': data, 'message': 'license key is valid'}
                    else:
                        return {'status': False, 'license': key, 'message': 'license key has been expired'}
            return {'status': False, 'license': key, 'message': 'license key is not valid'}
        except Exception as error:
            raise Exception(str(error))