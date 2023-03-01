from django.forms import ModelForm
from django.forms.utils import ErrorList

from main.models import Child


class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = '__all__'

    def clean(self):
        room = self.cleaned_data.get('room', None)
        num_child = Child.objects.filter(room=room).count()
        expedient = self.cleaned_data.get('expedient', None)
        has_expedient = Child.objects.filter(expedient=expedient)
        if room and num_child >= 30:
            self._errors['room'] = ErrorList(['No se puede tener mas de 30 niños en un salon'])
        if expedient and has_expedient:
            self._errors['expedient'] = ErrorList(['El expediente ya esta asignado'])
        return self.cleaned_data
