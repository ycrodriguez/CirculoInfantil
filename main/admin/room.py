from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.views.generic import DetailView

from main.models import *
from CirculoInfantil.functions import exportPDF


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ['code_room', 'room_number']
    list_display = ['code_room', 'room_number', 'inventario', 'registro']
    change_list_template = 'admin/change_list_template.html'

    def inventario(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="Inventario" style="color:green;" class="related-widget-wrapper-link add-related" href="pdf/inventario/{}/"><i class="fa fa-file-pdf"></i></a>'.format(
                    obj.pk))
        return None

    def registro(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="registro" style="color:red;" class="related-widget-wrapper-link add-related" href="pdf/registro/{}/"><i class="fa fa-file-pdf"></i></a>'.format(
                    obj.pk))
        return None

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('pdf/inventario/<int:pk>/', self.inventario_pdf_view.as_view(), name='inventario'),
                   path('pdf/registro/<int:pk>/', self.matricula_pdf_view.as_view(), name='registro')
               ] + urls
        return urls

    class inventario_pdf_view(DetailView):
        def get(self, request, *args, **kwargs):
            room = kwargs.get('pk', None)
            return exportPDF('pdf/salon_inventario/data.html',
                             '{}'.format('PDF Inventario'),
                             {
                                 'request': request,
                                 'articulos': Article.objects.filter(room__pk=room),
                                 'room': Room.objects.get(pk=room)
                             }
                             )

    class matricula_pdf_view(DetailView):
        def get(self, request, *args, **kwargs):
            room = kwargs.get('pk', None)
            return exportPDF('pdf/matricula_salon/data.html',
                             '{}'.format('PDF Inventario'),
                             {
                                 'request': request,
                                 'childs': Child.objects.filter(room__pk=room),
                                 'room': Room.objects.get(pk=room)
                             }
                             )
