from django.urls import path, re_path
from django.conf.urls import include

from documentos.views import DocAnalisisView

urlpatterns = [
    re_path(r'doc_analisis$', DocAnalisisView.as_view()),
]