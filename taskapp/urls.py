from django.contrib import admin
from django.urls import include, path
from .views import *

#urlpatterns = [
#    path('',ImageList.as_view()),
#    path('<int:pk>',ImageDetail.as_view()),
#]
from django.conf.urls import url
from .views import FileView
urlpatterns = [
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^view/$', ImageList.as_view()),
    url(r'^detail/$', ImageDetail.as_view()),

]