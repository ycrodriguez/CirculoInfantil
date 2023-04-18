from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.utils import timezone
from django.utils.html import format_html
from django.views.generic import DetailView, ListView, CreateView

from main.models import *
from main.form.attendance import AttendanceForm, FechaSelect
from CirculoInfantil.functions import exportPDF


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ['code_room', 'room_number']
    list_display = ['code_room', 'room_number', 'inventario', 'registro', 'asistencia']

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

    def asistencia(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="asistencia" style="color:blue;" class="related-widget-wrapper-link add-related" href="asistencia/{}/"><i class="fa fa-circle"></i></a>'.format(
                    obj.pk))
        return None

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('pdf/inventario/<int:pk>/', self.inventario_pdf_view.as_view(), name='inventario'),
                   path('pdf/registro/<int:pk>/', self.matricula_pdf_view.as_view(), name='registro'),
                   path('asistencia/<int:pk>/', self.asistencia_view.as_view(), name='asistencia'),
               ] + urls
        return urls

    class inventario_pdf_view(DetailView):
        def get(self, request, *args, **kwargs):
            room = kwargs.get('pk', None)
            return exportPDF('pdf/salon_inventario/data.html',
                             '{}'.format('PDF Inventario'),
                             {
                                 'request': request,
                                 'data': timezone.now(),
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
                                 'data': timezone.now(),
                                 'childs': Child.objects.filter(room__pk=room),
                                 'room': Room.objects.get(pk=room)
                             }
                             )

    class asistencia_view(ListView, CreateView):
        def get(self, request, *args, **kwargs):
            room_pk = kwargs.get('pk', None)
            attendences = Attendance.objects.filter(attendance_date__day=timezone.now().day,
                                                    attendance_date__month=timezone.now().month,
                                                    attendance_date__year=timezone.now().year)
            forms = [{
                "child": obj,
                "form": AttendanceForm(prefix=obj.pk, initial={
                    'type': attendences.filter(child=obj).last().type if attendences.filter(
                        child=obj).last() else None
                })
            } for obj in Child.objects.filter(room__pk=room_pk)]

            return render(request, 'custom/attendance_form.html', {
                'num_room': Room.objects.get(pk=room_pk),
                'room_pk': room_pk,
                'forms': forms,
                "fecha": FechaSelect(prefix='fecha', initial={
                    'fecha': attendences.last().attendance_date if attendences.count() > 0 else None
                })
            })

        def post(self, request, *args, **kwargs):
            room_pk = kwargs.get('pk', None)
            childs = Child.objects.filter(room__pk=room_pk)
            fecha = timezone.now().date()
            if "fecha-fecha" in request.POST:
                form = FechaSelect(request.POST, prefix='fecha')
                if form.is_valid():
                    fecha = form.cleaned_data['fecha']
            for child in childs:
                if "{}-type".format(child.pk) in request.POST:
                    form = AttendanceForm(request.POST, prefix=child.pk)
                    if form.is_valid():
                        type = form.cleaned_data['type']
                        obj, created = Attendance.objects.get_or_create(child=child, attendance_date=fecha)
                        if obj.type != type:
                            obj.type = type
                            obj.save()
            return redirect('/main/room/')
