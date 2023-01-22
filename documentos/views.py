from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pathlib import Path

import os, datetime, time
import pandas as pd
import matplotlib.pyplot as plt


from documentos.serializers import doc_analisis_Serializer1
from documentos.PDFclass import PDF

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
class DocAnalisisView(APIView):

    def save_pdf(self, data):
        fecha = datetime.datetime.now().strftime('%d-%m-%Y')
        base_dir = str(BASE_DIR)
        base_dir2 = base_dir.replace('\\', '/')

        doc_data = [
        ["ID del documento:", data.get('identificador', None)],
        ["Responsable:", data.get('usuario', None)],
        ["Fecha:", fecha],
        ]
        pdf = PDF(data.get('usuario', None))
        
        pdf.add_title(data.get('nombre', None))
        pdf.add_subtitle("Proceso")
        pdf.add_table(doc_data)
        pdf.add_text('Objetivo: '+ data.get('objetivo', None))
        pdf.add_text('Indicadores y métricas: ' + data.get('ind_met', None))
        pdf.add_text('Descripción de actividades: ' + data.get('des_actividades', None))
        pdf.add_image(base_dir2+data.get('diagrama_flujo', None))
        pdf.add_text('Categoria: '+ data.get('categoria', None))
        pdf.add_text('Evidencias de salida: '+ data.get('salida', None))
        pdf.add_text('Frecuencia: '+ data.get('frecuencia', None))
  
        doc_path = base_dir2+f"/assets/archivosPDF/analisis_diseño/{data.get('identificador', None)}_{fecha}.pdf"
        pdf.output(doc_path)
        print("PDF guardado")
     

    def post(self, request):
        serializer = doc_analisis_Serializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.save_pdf(serializer.data)
            return Response( serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
