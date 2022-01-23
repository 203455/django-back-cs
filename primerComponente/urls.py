from django import views
from django.urls import path, re_path
from django.conf.urls import include

#importamos view
from primerComponente.views import PrimerTablaList

urlpatterns = [
    re_path(r'^primer_componente/$', PrimerTablaList.as_view()),
]


