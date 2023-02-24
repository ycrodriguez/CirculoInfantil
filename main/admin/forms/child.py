from django.forms import ModelForm
from django.forms.utils import ErrorList

from main.models import Child


class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = 'room'

    def clean(self):
        room = self.cleaned_data.get('room', None)
        num_child = Child.objects.filter(room=room).count()
        if room and num_child > 30:
            self._errors['room'] = ErrorList(['No se puede tener mas de 30 niños en un salon'])
        return super().clean()
