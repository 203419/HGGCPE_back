from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pathlib import Path
from django.http import FileResponse, HttpResponse

import os, datetime, time
import pandas as pd
import matplotlib.pyplot as plt


from documentos.serializers import doc_analisis_Serializer1, doc_pruebasU_Serializer, doc_requisitos_Serializer
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
        ["Responsable del doc.:", data.get('usuario', None)],
        ["Fecha:", fecha],
        ]
        pdf = PDF(data.get('usuario', None))
        
        pdf.add_title("Documento de Análisis y Diseño")
        pdf.add_subtitle("Proceso "+ data.get('nombre', None))
        pdf.add_table(doc_data)
        pdf.add_text('Objetivo: '+ data.get('objetivo', None))
        pdf.add_text('Indicadores y métricas: \n' + data.get('ind_met', None))
        pdf.add_text('Descripción de actividades: \n' + data.get('des_actividades', None))
        pdf.add_image(base_dir2+data.get('diagrama_flujo', None))
        pdf.add_text('Categoria: '+ data.get('categoria', None))
        pdf.add_text('Evidencias de salida: \n'+ data.get('salida', None))
        pdf.add_text('Frecuencia: '+ data.get('frecuencia', None))
        pdf.add_subtitle("Evidencia")
        pdf.add_text('Introducción: '+ data.get('introE', None))
        pdf.add_text('Alcance: '+ data.get('alcanceE', None))
        pdf.add_text('Objetivos: \n'+ data.get('objetivosE', None))
        pdf.add_text("Arquitectura")
        pdf.add_image(base_dir2+data.get('arq1', None))
        try:
            if data.get('arq2', None) != "None":
                pdf.add_image(base_dir2+data.get('arq2', None))
            if data.get('arq3', None) != "None":
                pdf.add_image(base_dir2+data.get('arq3', None))
        except:
            print("None")

        pdf.add_text("Componentes")
        pdf.add_image(base_dir2+data.get('comp1', None))
        try:
            if data.get('comp2', None) != "None":
                pdf.add_image(base_dir2+data.get('comp2', None))
            if data.get('comp3', None) != "None":
                pdf.add_image(base_dir2+data.get('comp3', None))
        except:
            print("None")

        pdf.add_text('Descripción de componentes: \n'+ data.get('des_componentesE', None))


        doc_name = f"{data.get('identificador', None)}_{fecha}.pdf"
        doc_path = base_dir2+f"/assets/archivosPDF/analisis_diseño/{doc_name}"
        pdf_data = []
        pdf_data.append(doc_name)
        pdf_data.append(doc_path)
        
        pdf.output(doc_path)
        print("PDF guardado")

        return pdf_data
     

    def post(self, request):
        serializer = doc_analisis_Serializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pdf_data = self.save_pdf(serializer.data)
            response = FileResponse(open(pdf_data[1], 'rb'))
            response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = f'attachment; filename={pdf_data[0]}'
            return HttpResponse(response, content_type='application/pdf', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocPruebasUniView(APIView):
    def save_pdf(self, data):
        fecha = datetime.datetime.now().strftime('%d-%m-%Y')
        base_dir = str(BASE_DIR)
        base_dir2 = base_dir.replace('\\', '/')

        doc_data = [
        ["ID del documento:", data.get('identificador', None)],
        ["Responsable del doc.:", data.get('usuario', None)],
        ["Fecha:", fecha],
        ]
        ev_data = [
        ["Encargado: ", data.get('encargado', None)],
        ["Fase: ", data.get('fase', None)],
        ["Lugar y fecha: ", data.get('lugar_fecha', None)],
        ]
        pdf = PDF(data.get('usuario', None))
        
        pdf.add_title("Reporte de pruebas unitarias")
        pdf.add_subtitle("Proceso "+ data.get('nombre_proceso', None))
        pdf.add_table(doc_data)
        pdf.add_text('Objetivo: '+ data.get('objetivo', None))
        pdf.add_text('Indicadores y métricas: \n' + data.get('ind_met', None))
        pdf.add_text('Descripción de actividades: \n' + data.get('des_actividades', None))
        pdf.add_image(base_dir2+data.get('diagrama_flujo', None))
        pdf.add_text('Categoria: '+ data.get('categoria', None))
        pdf.add_text('Evidencias de salida: \n'+ data.get('salida', None))
        pdf.add_text('Frecuencia: '+ data.get('frecuencia', None))
        pdf.add_subtitle("Evidencias" + data.get('nombre_proyecto', None))
        pdf.add_table(ev_data)
        pdf.add_text('Requerimientos para el código: \n'+ data.get('req', None))
        pdf.add_text('Repositorio Github: '+ data.get('repo', None))
        pdf.add_text('Nombre de la selección: '+ data.get('selec', None))
        pdf.add_text("Código")
        pdf.add_image(base_dir2+data.get('cod1', None))
        try:
            if data.get('cod2', None) != "None":
                pdf.add_image(base_dir2+data.get('cod2', None))
            if data.get('cod3', None) != "None":
                pdf.add_image(base_dir2+data.get('cod3', None))
        except:
            print("None")

        pdf.add_text('Lineas de código: '+ data.get('lineas', None))


        doc_name = f"{data.get('identificador', None)}_{fecha}.pdf"
        doc_path = base_dir2+f"/assets/archivosPDF/pruebas_unitarias/{doc_name}"
        pdf_data = []
        pdf_data.append(doc_name)
        pdf_data.append(doc_path)
        
        pdf.output(doc_path)
        print("PDF guardado")

        return pdf_data
     

    def post(self, request):
        serializer = doc_pruebasU_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pdf_data = self.save_pdf(serializer.data)
            response = FileResponse(open(pdf_data[1], 'rb'))
            response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = f'attachment; filename={pdf_data[0]}'
            return HttpResponse(response, content_type='application/pdf', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocRequisitosView(APIView):
    def save_pdf(self, data):
        fecha = datetime.datetime.now().strftime('%d-%m-%Y')
        base_dir = str(BASE_DIR)
        base_dir2 = base_dir.replace('\\', '/')

        doc_data = [
        ["ID del documento:", data.get('identificador', None)],
        ["Responsable del doc.:", data.get('usuario', None)],
        ["Fecha:", fecha],
        ]
        
        pdf = PDF(data.get('usuario', None))
        
        pdf.add_title("Documento de requisitos")
        pdf.add_subtitle("Proceso "+ data.get('nombre_proceso', None))
        pdf.add_table(doc_data)
        pdf.add_text('Objetivo: '+ data.get('objetivo', None))
        pdf.add_text('Indicadores y métricas: \n ' + data.get('ind_met', None))
        pdf.add_text('Descripción de actividades: \n ' + data.get('des_actividades', None))
        pdf.add_text('Categoria: '+ data.get('categoria', None))
        pdf.add_text('Evidencias de salida: \n '+ data.get('salida', None))
        pdf.add_text('Frecuencia: '+ data.get('frecuencia', None))
        pdf.add_subtitle("Evidencias")
        pdf.add_text('Proposito: '+ data.get('proposito', None))
        pdf.add_text('Alcance: '+ data.get('alcance', None))
        pdf.add_text("Referencias ")
        pdf.add_image(base_dir2+data.get('referencias', None))
        pdf.add_text("Funcionalidades del producto: "+ data.get('funcionalidades', None))
        pdf.add_text('Clases y caracteristicas del usuario: '+ data.get('clases', None))
        pdf.add_text('Entorno operativo: '+ data.get('entorno', None))
        pdf.add_text('Requisitos funcionales: \n '+ data.get('req_f', None))
        pdf.add_text('Requisitos no funcionales: \n '+ data.get('req_nf', None))

        doc_name = f"{data.get('identificador', None)}_{fecha}.pdf"
        doc_path = base_dir2+f"/assets/archivosPDF/requisitos/{doc_name}"
        pdf_data = []
        pdf_data.append(doc_name)
        pdf_data.append(doc_path)
        
        pdf.output(doc_path)
        print("PDF guardado")

        return pdf_data
     

    def post(self, request):
        serializer = doc_requisitos_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pdf_data = self.save_pdf(serializer.data)
            response = FileResponse(open(pdf_data[1], 'rb'))
            response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = f'attachment; filename={pdf_data[0]}'
            return HttpResponse(response, content_type='application/pdf', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)