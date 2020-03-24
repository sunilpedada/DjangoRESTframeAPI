from django.conf.urls import url
from.views import employees
urlpatterns=[
    url(r"^api/$",employees.as_view()),
]