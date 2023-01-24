from django.urls import path, re_path
from django.conf.urls import include

from documentos.views import DocAnalisisView, DocPruebasUniView, DocRequisitosView

urlpatterns = [
    re_path(r'doc_analisis$', DocAnalisisView.as_view()),
    re_path(r'doc_pruebas_uni$', DocPruebasUniView.as_view()),
    re_path(r'doc_requisitos$', DocRequisitosView.as_view()),
]