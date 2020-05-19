#coding:utf-8

import requests
import base64
import json

t_user = 'fuck123fuckabc'
t_tokens='86cc04ed257bcfa0144eb69bb734bfd35a297319'
t_proj = 'test'
t_path = 'tw'
t_file = '1234.txt'

#url = "https://api.github.com/repos/[user]/[proj]/contents/[path]/"+ fn
url = "https://api.github.com/repos/{}/{}/contents/{}/{}".format(t_user, t_proj, t_path, t_file)

print 'upload', url

d = {
   "message": "my commit message",
   "content": base64.b64encode("123456").decode('utf-8'),
   "sha": ""
}
headers = {"Authorization": 'token '+t_tokens} 
r = requests.put(url=url,data=json.dumps(d), headers=headers)
print r.status_code   # 201 ok, 422 重复
print r.text
###############################################
print '\nget info'
r = requests.get(url=url)
print r.status_code   
print r.text
t_sha = json.loads(r.text)['sha']
print t_sha


print '\nupdate info'
d = {
   "message": "my commit message",
   "content": base64.b64encode("77777777").decode('utf-8'),
   "sha": t_sha
}
headers = {"Authorization": 'token '+t_tokens} 
r = requests.put(url=url,data=json.dumps(d), headers=headers)
print r.status_code   
print r.text

r = requests.get(url=url)
t_sha = json.loads(r.text)['sha']
print t_sha


print '\ndelete file'
d = {
   "message": "my commit message",
   "sha": t_sha
}
headers = {"Authorization": 'token '+t_tokens} 
r = requests.delete(url=url,data=json.dumps(d), headers=headers)
print r.status_code   
print r.text





