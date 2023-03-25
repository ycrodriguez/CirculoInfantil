import re
from django.forms import ModelForm
from django.forms.utils import ErrorList

from main.models import Child, Expedient


class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)
        if self.fields.get('expedient', None):
            self.fields['expedient'].queryset = Expedient.objects.filter(child__isnull=True)

    def clean(self):
        room = self.cleaned_data.get('room', None)
        ci = self.cleaned_data.get('ci_child', None)
        eyesColor = self.cleaned_data.get('eyes_color', None)
        hairColor = self.cleaned_data.get('hair_color', None)
        skinColor = self.cleaned_data.get('skin_color', None)
        expediente = self.cleaned_data.get('expedient', None)

        num_child = Child.objects.filter(room=room).count()
        has_expedient = Child.objects.filter(expedient=expediente)
        eyesColor_has_number = re.findall('[0-9]+', eyesColor)
        hairColor_has_number = re.findall('[0-9]+', hairColor)
        skinColor_has_number = re.findall('[0-9]+', skinColor)

        if room and num_child >= 30:
            self._errors['room'] = ErrorList(['Solo se permiten letras'])
        if eyesColor_has_number:
            self.errors['eyes_color'] = ErrorList(['Solo se permiten letras'])
        if hairColor_has_number:
            self.errors['hair_color'] = ErrorList(['Solo se permiten letras'])
        if skinColor_has_number:
            self.errors['skin_color'] = ErrorList(['Solo se permiten letras'])
        if not ci.isdigit():
            self.errors['ci_child'] = ErrorList(['Solo se permiten números'])
        return self.cleaned_data
