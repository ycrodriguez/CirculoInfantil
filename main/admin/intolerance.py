from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.views.generic import DetailView

from main.models import *
from CirculoInfantil.functions import exportPDF


@admin.register(Intolerance)
class IntoleranceAdmin(admin.ModelAdmin):
    search_fields = ['name_intolerance']
    list_display = ['name_intolerance', 'description_intolerance', 'reporte_de_intolerancia']
    change_list_template = 'admin/change_list_template.html'

    def reporte_de_intolerancia(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="Intolerancias" style="color:green;" class="related-widget-wrapper-link add-related" href="pdf/reporte_intolerancia/{}/"><i class="fa fa-file-pdf"></i></a>'.format(
                    obj.pk))
        return None

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('pdf/reporte_intolerancia/<int:pk>/', self.reporte_intolerancia_pdf.as_view(),
                        name='reporte_intolerancia_pdf')
               ] + urls
        return urls

    class reporte_intolerancia_pdf(DetailView):
        def get(self, request, *args, **kwargs):
            intolerancia = kwargs.get('pk', None)
            return exportPDF('pdf/intolerancia_expediente/data.html',
                             '{}'.format("PDF Reporte por intolerancias"),
                             {
                                 'request': request,
                                 'childs': Child.objects.filter(intolerance__pk=intolerancia),
                                 'intole': Intolerance.objects.get(pk=intolerancia),
                             }
                             )
