from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunctioncall, name="index"),
    path('about', views.myfunctionabout, name="about"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),
    path('mycommonpage',views.mycommonpage,name="mycommonpage"),
]

