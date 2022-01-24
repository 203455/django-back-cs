from django.urls import path, re_path

#importamos view
from Register.views import UserApi

urlpatterns = [
    re_path(r'^create', UserApi.as_view()),
]