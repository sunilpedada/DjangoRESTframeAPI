import json
import requests
def getWith_id_or_none(id=None):
    data={}
    if id is not None:
        data={"id":id}
    response=requests.get("http://127.0.0.1:8000/api/api/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
getWith_id_or_none()