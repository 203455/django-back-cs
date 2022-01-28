from django import views
from django.urls import path, re_path
from django.conf.urls import include

#importamos view
from primerComponente.views import PrimerTablaList
from primerComponente.views import PrimerTablaDetails

urlpatterns = [
    re_path(r'^lista/$', PrimerTablaList.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', PrimerTablaDetails.as_view()),
]


