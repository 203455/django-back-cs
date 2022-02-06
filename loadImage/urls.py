from django import views
from django.urls import path, re_path
from django.conf.urls import include

#importamos view
from loadImage.views import LoadImageTable
from loadImage.views import LoadImageTableDetail

urlpatterns = [
    re_path(r'^imagenes/$', LoadImageTable.as_view()),
    re_path(r'^imagenes/(?P<pk>\d+)$', LoadImageTableDetail.as_view()),
]