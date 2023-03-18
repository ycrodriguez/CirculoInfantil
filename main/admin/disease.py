from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.views.generic import DetailView

from CirculoInfantil.functions import exportPDF
from main.models import *


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ['name_disease']
    list_display = ['name_disease', 'description_disease', 'reporte_de_enfermedades']
    change_list_template = 'admin/change_list_template.html'

    def reporte_de_enfermedades(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="Enfermedades" style="color:green;" class="related-widget-wrapper-link add-related" href="pdf/reporte_enfermedades/{}/"><i class="fa fa-file-pdf"></i></a>'.format(
                    obj.pk))
        return None

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('pdf/reporte_enfermedades/<int:pk>/', self.reporte_enfermedades_pdf.as_view(),
                        name='reporte_enfermedades_pdf')
               ] + urls
        return urls

    class reporte_enfermedades_pdf(DetailView):
        def get(self, request, *args, **kwargs):
            enfermedad = kwargs.get('pk', None)
            return exportPDF('pdf/enfermedad_expediente/data.html',
                             '{}'.format("PDF Reporte por enfermedades"),
                             {
                                 'request': request,
                                 'childs': Child.objects.filter(diseases__pk=enfermedad),
                                 'enferm': Disease.objects.get(pk=enfermedad),
                             }
                             )
