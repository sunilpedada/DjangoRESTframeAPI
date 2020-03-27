from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from.models import EmployeDetails
from.serializing import EmployeSerializer,testserializer
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.
#Note:cmd:pip freeze>requirements.txt(for write required softwars) 
# cmd: type requirements.txt (to read )
# cmd : pip install -r requirements.txt (to install)
@method_decorator(csrf_exempt,name='dispatch')
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
    def post(self,request,*args,**kwargs):
        data=io.BytesIO(request.body)
        jason_load=JSONParser().parse(data)
        serialized=EmployeSerializer(data=jason_load)
        if serialized.is_valid():
            serialized.save()
            msg={"msg":"record inserted"}
            json_dump=JSONRenderer().render(msg)
            return HttpResponse(json_dump,content_type="application/json",status=201)
        json_dump=JSONRenderer().render(serialized.errors)
        return HttpResponse(json_dump,content_type="application/json",status=400)
    def put(self,request,*args,**kwargs):
        data=io.BytesIO(request.body)
        jason_load=JSONParser().parse(data)
        get_id=jason_load.get("id")
        get_instance=EmployeDetails.objects.get(id=get_id)
        serialized=EmployeSerializer(get_instance,data=jason_load,partial=True)
        if serialized.is_valid():
            serialized.save() 
            msg={"msg":"record updated"}
            json_dump=JSONRenderer().render(msg)
            return HttpResponse(json_dump,content_type="application/json",status=201)
        json_dump=JSONRenderer().render(serialized.errors)
        return HttpResponse(json_dump,content_type="application/json",status=400)
    def delete(self,request,*args,**kwargs):
        data=io.BytesIO(request.body)
        jason_load=JSONParser().parse(data)
        get_id=jason_load.get("id")
        get_instance=EmployeDetails.objects.get(id=get_id)
        get_instance.delete()
        msg={"msg":"record deleted"}
        json_dump=JSONRenderer().render(msg)
        return HttpResponse(json_dump,content_type="application/json",status=200)

# #/////////////////// DRFviews => APIView ////////////////////////////////////
class testAPIView(APIView):
    def get(self,request,*args,**kwargs):
        data={"name":"sunil","no":420}
        return Response(data,status=200)
    def post(self,request,*args,**kwargs):
        serialized_data=testserializer(data=request.data)
        if serialized_data.is_valid():
            get_name=serialized_data.data.get("name")
            msg="hello {} welcome to drf".format(get_name)
            return Response(msg,status=200)
        return Response(serialized_data.errors,status=400)
    def put(self,request,*args,**kwargs):
        data={"name":"sunil","no":420}
        return Response(data,status=200)
    def patch(self,request,*args,**kwargs):
        data={"name":"sunil","no":420}
        return Response(data,status=200)
    def delete(self,request,*args,**kwargs):
        data={"name":"sunil","no":420}
        return Response(data,status=200)

# class testAPIView(APIView):
#     def get(self,request,format=None):
#         data=EmployeDetails.objects.all()
#         serialized=EmployeSerializer(data,many=True)
#         return Response(serialized.data,status=200)

# /////////////////////////////////////////////////////////////////////////
# class testViewset(ViewSet):
#     def list():
#     def retrieve():
#     def create():
#     def update():
#     def partial_update():
#     def destroy():