from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from.models import EmployeDetails
from.serializing import EmployeSerializer
from django.http import HttpResponse
# Create your views here.
#Note:cmd:pip freeze>requirements.txt(for write required softwars) 
# cmd: type requirements.txt (to read )
# cmd : pip install -r requirements.txt (to install)
class employees(View):
    def get(self,request,*args,**kwargs):
        data=io.BytesIO(request.body)
        json_format=JSONParser().parse(data)
        get_id=json_format.get("id",None)
        if get_id is not None:
            record=EmployeDetails.objects.get(id=get_id)
            serialized=EmployeSerializer(record)
            json_render=JSONRenderer().render(serialized.data)
            return HttpResponse(json_render,content_type='application/json',status=200)
        get_all=EmployeDetails.objects.all()
        serialized=EmployeSerializer(get_all,many=True)
        json_render=JSONRenderer().render(serialized.data)
        return HttpResponse(json_render,content_type='application/json',status=200)

