import json
import requests
def getWith_id_or_none(id=None):
    data={}
    if id is not None:
        data={"id":id}
    response=requests.get("http://127.0.0.1:8000/api/api/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
def post():
    data={"ename":"wxxx","email":"wxx@ff.com","esalary":1000}
    response=requests.post("http://127.0.0.1:8000/api/api/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
def update(id):
    data={"id":id,"ename":"zggg","email":"ze@ff.com"}
    response=requests.put("http://127.0.0.1:8000/api/api/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
def delete(id):
    data={"id":id}
    response=requests.delete("http://127.0.0.1:8000/api/api/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
post()
