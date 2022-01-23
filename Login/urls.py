from django.urls import path, re_path
from django.conf.urls import include

#importamos view
from Login.views import loginAuth

urlpatterns = [
    re_path(r'^', loginAuth.as_view()),
]