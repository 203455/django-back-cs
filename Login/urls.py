from django.urls import path, re_path
from django.conf.urls import include

#importamos view
from Login.views import loginAuth
from Login.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    re_path(r'^v1/login', loginAuth.as_view()),
    re_path(r'^v2/login', MyObtainTokenPairView.as_view()),
    re_path(r'v2/refresh/', TokenRefreshView.as_view()),

]