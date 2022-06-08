from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,name="index"),
    path("allurls/",views.allurls,name="allurls"),
    path("shorturl/<int:id>/",views.get_url,name="shorturl"),
    path("shorten/",views.shorten,name="shorten"),
]