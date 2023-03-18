import re
from django.forms import ModelForm
from django.forms.utils import ErrorList
from django.core.validators import RegexValidator

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
        expediente = self.cleaned_data.get('expedient', None)
        eyesColor = self.cleaned_data.get('eyes_color', None)
        hairColor = self.cleaned_data.get('hair_color', None)
        skinColor = self.cleaned_data.get('skin_color', None)
        num_child = Child.objects.filter(room=room).count()
        has_expedient = Child.objects.filter(expedient=expediente)
        ci_has_number = re.findall('[0-9]+', ci)
        eyesColor_has_number = re.findall('[0-9]+', eyesColor)
        hairColor_has_number = re.findall('[0-9]+', hairColor)
        skinColor_has_number = re.findall('[0-9]+', skinColor)

        if room and num_child >= 30:
            self._errors['room'] = ErrorList(['No se puede tener mas de 30 niños en un salon'])
        if eyesColor_has_number:
            self.errors['eyes_color'] = ErrorList(['No se permiten caracteres numéricos'])
        if hairColor_has_number:
            self.errors['hair_color'] = ErrorList(['No se permiten caracteres numéricos'])
        if skinColor_has_number:
            self.errors['skin_color'] = ErrorList(['No se permiten caracteres numéricos'])
        if not ci_has_number:
            self.errors['ci_child'] = ErrorList(['No se permiten letras'])
        return self.cleaned_data
