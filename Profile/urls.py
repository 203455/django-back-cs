from django import views
from django.urls import path, re_path
from django.conf.urls import include

#importamos view
from Profile.views import LoadProfileTable
from Profile.views import LoadProfileTableDetail

urlpatterns = [
    re_path(r'^imagenes/$', LoadProfileTable.as_view()),
    re_path(r'^imagenes/(?P<pk>\d+)$', LoadProfileTableDetail.as_view()),
]