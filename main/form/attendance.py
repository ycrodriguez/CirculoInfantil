from django import forms
from main.models import Attendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('type',)
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control input-md'}),
        }


class FechaSelect(forms.Form):
    fecha = forms.CharField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
