from django.conf.urls import url,include
from.views import employees,testAPIView
# from rest_framework.routers import DefaultRouter
# routerObj=DefaultRouter()
# routerObj.register("testViewset",views.testViewset,base_name="testViewset")
urlpatterns=[
    url(r"^api/$",employees.as_view()),
    url(r"^test/$",testAPIView.as_view()),
    # url(r'',include(routerObj.urls))
]